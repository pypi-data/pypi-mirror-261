import logging
import coloredlogs
import colorama
from colorama import Fore, Style
import os
if not os.path.exists("logs"):
    os.makedirs("logs")
colorama.init()
class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_level_color = {
            'INFO': Fore.WHITE,
            'DEBUG': Fore.BLUE,
            'WARNING': Fore.YELLOW,
            'ERROR': Fore.RED,
            'CRITICAL': Fore.RED
        }
        log_time = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        log_level = record.levelname
        log_msg = record.msg

        log_format = f"{log_time} {log_level_color[log_level]}{log_level}{Style.RESET_ALL} {log_msg}"
        return log_format
logger = logging.getLogger('OneBotWS')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('./logs/log.log')
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
custom_formatter = CustomFormatter()
console_handler.setFormatter(custom_formatter)
logger.addHandler(console_handler)
coloredlogs.install(level='DEBUG', logger=logger,fmt = '[%(asctime)s][%(levelname)s] %(message)s')