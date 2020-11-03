# ！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===========================
# @Time : 2020/10/31 23:22
# @File  : log_settings.py
# @Author: adeng
# @Date  : 2020/10/31
============================
"""
import os
import logging.config



# 定义三种日志输出格式 开始

standard_format = '%(asctime)s-%(threadName)s:%(thread)d-task_id:%(name)s-%(filename)s:%(lineno)d-' \
                  '%(funcName)s-%(levelname)s-%(message)s' #其中name为getlogger指定的名字

simple_format = '%(levelname)s-task_id:%(name)s-%(asctime)s-%(filename)s:%(lineno)d-%(message)s'

id_simple_format = '%(asctime)s-%(levelname)s-%(message)s'

# 定义日志输出格式 结束
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
logfile_dir = LOG_DIR # log文件的目录

logfile_name = 'test_case.log'  # log文件名
logfile_error_name = "software_error.log"

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)
logfile_error_path = os.path.join(logfile_dir, logfile_error_name)
logfile_other_path = os.path.join(logfile_dir, "other01.log")

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        #打印到文件的日志:收集错误及以上的日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': logfile_error_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console','error', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,  #True 向上（更高level的logger）传递
        },
        # 下面实例化收集器名为adeng， 初始化必须一样才会触发。logging.getLogger("adeng")
        "adeng":{
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False, #默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        }
    },
}

def load_my_logging_cfg(name):
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(name)  # 生成一个log实例
    return logger
logger = load_my_logging_cfg

if __name__ == '__main__':
    logger("支付接口").error("XX参数错误")
    logger("登录").info("账号或者密码错误")
