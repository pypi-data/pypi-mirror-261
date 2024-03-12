from lightningrobot.adapter import Adapter
from lightningrobot import log
import websocket
import signal
from lightningrobot_adapter_onebot.core import *
from lightningrobot_adapter_onebot.utils.logger import logger, logging


ws_url = "ws://127.0.0.1:3001"
ws = websocket.WebSocketApp(ws_url)
def stop(sig, frame):
    logger.info(">>> 正在关闭监听......")
    ws.keep_running = False
    logger.info(">>> 正在关闭日志记录器......")
    logging.shutdown()
    exit(0)

    

class OnebotAdapter(Adapter):
    async def connect(self) -> None:
        log.info("已加载-OnebotAdapter")
        pass

    async def send_message(self, message: str) -> None:
        print("未完善发送信息")

    async def listen(self) -> str:
        signal.signal(signal.SIGINT, stop)
        ws.on_message = on_message
        ws.run_forever()