from pathlib import Path
from playwright.async_api import Page
from playwright.async_api import Response
from playwright_stealth import stealth_async
import pickle
import json
import websockets
import base64
import asyncio
import time

from .config import MsgData,Session,SetCookieParam,Status
from .OpenAIAuth import AsyncAuth0

class MockResponse:
    def __init__(self, data, status=200):
        self.data = data
        self.status = status
    
    async def text(self):
        return self.data

async def async_send_msg(page: Page,msg_data: MsgData,url: str,logger):
    '''msg send handle func'''
    ws = None
    if msg_data.last_wss != "":
        split_jwt = msg_data.last_wss.split('access_token=')[1].split('.')
        payload = split_jwt[1]
        padding = '=' * (4 - len(payload) % 4)
        decoded_payload = base64.urlsafe_b64decode(payload + padding)
        payload_data = json.loads(decoded_payload)
        now_time = int(time.time())
        if now_time < payload_data["exp"]:
            try:
                ws = await websockets.connect(msg_data.last_wss,user_agent_header=None)
            except Exception as e:
                logger.warning(f"open last wss error:{e}")
    async with page.expect_response(url,timeout=60000) as response_info:
        try:
            logger.info(f"send:{msg_data.msg_send}")
            await page.goto(url, timeout=60000)
        
        except Exception as e:
            
            if "Download is starting" not in e.args[0]:
                logger.warning(f"send msg error:{e}")
                raise e
            await page.wait_for_load_state("load")
            if response_info.is_done():
                return await response_info.value
        else:
            tmp = await response_info.value
            wss = json.loads(await tmp.text())
            wss_url = wss["wss_url"]
            msg_data.last_wss = wss_url
            data_list = []
            if ws:
                try:
                    while 1:
                        recv = await asyncio.wait_for(ws.recv(),timeout=20)
                        if json.loads(recv)["body"] == "ZGF0YTogW0RPTkVdCgo=":
                            break
                        data_list.append(recv)
                except Exception as e:
                    logger(f"error: {e}")
                    async with websockets.connect(wss_url,user_agent_header=None) as websocket:
                        while 1:
                            recv = await asyncio.wait_for(websocket.recv(),timeout=20)
                            if json.loads(recv)["body"] == "ZGF0YTogW0RPTkVdCgo=":
                                break
                            data_list.append(recv)
                finally:
                    await ws.close()
            else:
                async with websockets.connect(wss_url,user_agent_header=None) as websocket:
                    
                    while 1:
                        recv = await asyncio.wait_for(websocket.recv(),timeout=20)
                        if json.loads(recv)["body"] == "ZGF0YTogW0RPTkVdCgo=":
                            break
                        data_list.append(recv)
                    
            if data_list == []:
                msg = await get_msg_from_history(page,msg_data,url,logger)
                return MockResponse(msg)
            body = json.loads([newdata for newdata in data_list if "message_id" in newdata][-1])
            data = base64.b64decode(body["body"]).decode('utf-8')
            return MockResponse(data)

async def get_msg_from_history(page: Page,msg_data: MsgData,url: str,logger):
    url_cid = url + '/' + msg_data.conversation_id
    async with page.expect_response(url_cid,timeout=60000) as response_info:
        try:
            # logger.info(f"send:{msg_data.msg_send}")
            await page.goto(url_cid, timeout=60000)
            tmp = await response_info.value
            text = await tmp.json()
            if msg_data.last_id in text["mapping"]:
                # msg = text["mapping"][msg_data.last_id]
                # return "data: " + json.dumps(msg)
                msg = list(text["mapping"].items())[-1][-1]
                if msg_data.last_id == msg["parent"]:
                    return "data: " + json.dumps(msg)

            return "error"
        except Exception as e:
            raise e
                    

            
def markdown_to_text(markdown_string):
    '''it's not work now'''
    # Remove backslashes from markdown string
    # markdown_string = re.sub(r'\\(.)', r'\1', markdown_string)
    # Remove markdown formatting
    # markdown_string = re.sub(r'([*_~`])', '', markdown_string)
    # markdown_string = re.sub(r'\\(.)', r'\1', markdown_string)
    return markdown_string

def stream2msgdata(stream_lines:list,msg_data:MsgData):
    for x in stream_lines[::-1]:
        # for x in stream_lines:
        if '"end_turn": true' not in x:
            continue
        msg = json.loads(x[6:])
        tmp = msg["message"]["content"]["parts"][0]
        msg_data.msg_recv = markdown_to_text(tmp)
        try:
            msg_data.conversation_id = msg["conversation_id"]
        except KeyError as e:
            pass
        except Exception as e:
            raise e
        msg_data.next_msg_id = msg["message"]["id"]
        msg_data.status = True
        msg_data.msg_type = "old_session"
        break
    return msg_data

async def recive_handle(session: Session,resp: Response,msg_data: MsgData,logger):
    '''recive handle stream to msgdata'''
    if resp.status == 200:
        stream_text = await resp.text()
        stream_lines = stream_text.splitlines()
        msg_data = stream2msgdata(stream_lines,msg_data)
        if msg_data.msg_recv == "":
            logger.warning("This content may violate openai's content policy")
            msg_data.msg_recv = "This content may violate openai's content policy"
        if not msg_data.status:
            msg_data.msg_recv = str(resp.status) + " or maybe stream not end"
    elif resp.status == 401:
        # Token expired and you need to log in again | token过期 需要重新登录
        logger.warning(f"{session.email} 401,relogin now")
        session.login_state = False
        session.access_token = ""
        await Auth(session,logger)
        msg_data.msg_recv = f"{session.email} 401,relogin last,pleases try send again."
    else:
        msg_data.msg_recv = str(resp.status) + "\n" + resp.status_text + "\n" + await resp.text()
    return msg_data



def create_session(**kwargs) -> Session:
    session_token = kwargs.get("session_token")
    if session_token and isinstance(session_token, str):
        kwargs["session_token"] = SetCookieParam(
            url="https://chat.openai.com",
            name="__Secure-next-auth.session-token",
            value=session_token
        )
    return Session(**kwargs)

async def retry_keep_alive(session: Session,url: str,chat_file: Path,logger,retry:int = 2) -> Session:
    if retry != 2:
        logger.info(f"{session.email} flush retry {retry}")
    if retry == 0:
        logger.info(f"{session.email} stop flush")
        return session
    retry -= 1
    
    if session.page:
        page = await session.browser_contexts.new_page() # type: ignore
        await stealth_async(page)
        try:
            async with page.expect_response(url, timeout=20000) as a:
                res = await page.goto(url, timeout=20000)
            res = await a.value

            if res.status == 403 and res.url == url:
                session = await retry_keep_alive(session,url,chat_file,logger,retry)
            elif res.status == 200 and res.url == url:
                logger.info(f"flush {session.email} cf cookie OK!")
                await page.wait_for_timeout(1000)
                cookies = await session.page.context.cookies()
                cookie = next(filter(lambda x: x.get("name") == "__Secure-next-auth.session-token", cookies), None)

                if cookie:
                    session.session_token = SetCookieParam(
                        url="https://chat.openai.com",
                        name="__Secure-next-auth.session-token",
                        value=cookie["value"] # type: ignore
                    ) # type: ignore
                    update_session_token(session,chat_file,logger)
                else:
                    # no session-token,re login
                    session.status = Status.Update.value
                token = await res.json()
                if "error" in token and session.status != Status.Logingin.value:
                    session.status = Status.Update.value

            else:
                logger.error(f"flush {session.email} cf cookie error!")
        except Exception as e:
            logger.warning(f"retry_keep_alive {retry},error:{e}")
        finally:
            await page.close()
    else:
        logger.error(f"error! session {session.email} no page!")
    return session


async def Auth(session: Session,logger):
    '''Auth account login func'''
    if session.email and session.password:
        auth = AsyncAuth0(email=session.email, password=session.password, page=session.page, # type: ignore
                            mode=session.mode,
                            browser_contexts=session.browser_contexts,
                            logger=logger,
                            help_email=session.help_email
                            # loop=self.browser_event_loop
                            )
        session.status = Status.Logingin.value
        cookie, access_token = await auth.get_session_token(logger)
        if cookie and access_token:
            session.session_token = cookie
            session.access_token = access_token
            session.status = Status.Login.value
            session.login_state = True
            logger.info(f"{session.email} login success")
        else:
            logger.warning(f"{session.email} login error,waiting for next try")
            session.status = Status.Update.value

    else:
        logger.info("No email or password")
        
                
def update_session_token(session: Session,chat_file: Path,logger):
    session_file = chat_file / "sessions" / session.email
    try:
        # tmp = copy.copy(session)
        tmp = Session()
        tmp.access_token = session.access_token
        tmp.email = session.email
        tmp.input_session_token = session.input_session_token
        tmp.last_active = session.last_active
        tmp.last_wss = session.last_wss
        tmp.mode = session.mode
        tmp.password = session.password
        tmp.session_token = session.session_token
        tmp.browser_contexts = None
        tmp.page = None
        with open(session_file,"wb") as file:
            pickle.dump(tmp, file)
        del tmp
    except Exception as e:
        logger.warning(f"save session_token error：{e}")

def get_session_token(session: Session,chat_file: Path,logger):
    session_file = chat_file / "sessions" / session.email
    try:
        with open(session_file, 'rb') as file:
            load_session: Session = pickle.load(file)
            session.session_token = load_session.session_token
            session.last_wss = load_session.last_wss
            return session
    except FileNotFoundError:
        return session
    except Exception as e:
        logger.warning(f"get session_token from file error : {e}")
        return session
            
