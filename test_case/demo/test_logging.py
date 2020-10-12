# -*- coding: utf-8 -*-
# @Project: guoya-api-test
# @Author: 小吴老师
# @Email: wuling@guoyasoft.com
# @Weichat: 875955899
# @Create time: 2019/11/24 11:23

from tools.report import log_tool
# logging.basicConfig(filename='../../reports/logger.log', level=logging.INFO)

def test_one():
    # logging.debug('debug message')
    # logging.info('info message')
    # logging.warn('warn message')
    # logging.error('error message')
    # logging.critical('critical message')
    log_tool.info('这是一个美化器测试')


