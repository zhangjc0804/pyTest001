from tools.api import request_tool
from tools.data import random_tool
from tools.report.log_fengzhuang import logger

import allure
@allure.epic('一级归类')
@allure.feature('二级归类')
@allure.story('三级归类')
@allure.title("注册用户")
def test_sign():
    url = 'qa.yansl.com:8084/signup'
    phone = random_tool.random_tell()
    pwd = random_tool.random_pwd()
    re_pwd = pwd
    user_name = random_tool.random_name_pinyin()
    num = random_tool.random_number(10, 99)
    req = {
        "phone": phone,
        "pwd": pwd,
        "rePwd": re_pwd,
        "userName": user_name + str(num)
    }

    resp = request_tool.post_json(url, json=req)
    resp_json = resp.json()
    code = resp_json['code']
    assert code == 2000
  #  logger('注册shibai').error('自知则知之')
    logger("注册").info("账号或者密码错误")



