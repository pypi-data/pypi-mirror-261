import websocket
import signal
from lightningrobot.adapter import Adapter
from lightningrobot import log
from lightningrobot_adapter_onebot.utils import send_message
from lightningrobot_adapter_onebot.core import *

ws = websocket.WebSocketApp("ws://127.0.0.1:3001")

class OneBotAdapter(Adapter):
    async def connect(self) -> None:
        log.info("已加载-OneBotAdapter")
        pass

    async def send_message(self, event_type, id, message: str) -> None:
        if event_type == "group":
            send_message.send_group_message("ws://127.0.0.1:3001",id,message)
        elif event_type == "private":
            send_message.send_private_message("ws://127.0.0.1:3001",id,message)

    def stop(sig, frame):
        log.info(">>> 正在关闭监听......")
        ws.keep_running = False
        log.info(">>> 正在关闭日志记录器......")
        exit(0)

    async def listen(self) -> str:
        def stop(sig, frame):
            log.info(">>> 正在关闭监听......")
            ws.keep_running = False
            log.info(">>> 正在关闭日志记录器......")
            exit(0)
        signal.signal(signal.SIGINT, stop)
        ws.on_message = on_adaptermessage
        ws.run_forever()