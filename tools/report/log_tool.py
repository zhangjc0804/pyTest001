import logging
from logging.handlers import TimedRotatingFileHandler
from tools.os import os_tool

"""
封装log方法
"""
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
root_path = os_tool.get_root_path() + 'logs/'
os_tool.mkdir(root_path)

handler = TimedRotatingFileHandler(root_path + 'info.log',when = 'd',interval = 1,backupCount=30,encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


handler2 = TimedRotatingFileHandler(root_path + 'error.log',when = 'd',interval = 1,backupCount=30,encoding='utf-8')
handler2.setLevel(logging.ERROR)
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler2.setFormatter(formatter2)
logger.addHandler(handler2)

handler3 = TimedRotatingFileHandler(root_path + 'warring.log',when = 'd',interval = 1,backupCount=30,encoding='utf-8')
handler3.setLevel(logging.WARNING)
formatter3 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler3.setFormatter(formatter)
logger.addHandler(handler3)

handler4 = logging.StreamHandler()
handler4.setLevel(logging.DEBUG)
formatter4 = logging.Formatter()
handler4.setFormatter(formatter4)
logger.addHandler(handler4)


def info(msg):
    logger.info(msg)


def debug(msg):
    logger.debug(msg)


def warning(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)

