import logging.config
from tools.report.log_settings import LOGGING_DIC
#from log_settings import ettings里面配置了日志配置

class HandleLogs:
    def __init__(self):
        # 加载日志配置文件
        logging.config.dictConfig(LOGGING_DIC)

    def logger(self,name):
        logger = logging.getLogger(name)
        return logger

logger = HandleLogs().logger
if __name__ == '__main__':
    logger("登录截图").info("登录截图成功")
    logger("支付").info("支付密码错误")
    logger("创建测试10个测试账号").error("测试账号文件不存在，创建失败")