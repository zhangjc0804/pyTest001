from tools.api import request_tool
import pytest
import allure
@allure.title("旧密码登录失败")
def test_oldlogin():
    url = 'http://qa.yansl.com:8084/login'
    req = {
        "pwd": "123456zjcq",
        "userName":"dru795"
    }
    resp = request_tool.post_json(url, json=req)
    resp_json = resp.json()
    code = resp_json['code']
    print(code)
    message = resp_json['message']
    assert   message =='登录失败,密码错误'

@allure.title("新密码登录成功")
def test_changedlogin():
    url = 'http://qa.yansl.com:8084/login'
    req = {
        "pwd": "123456zjc",
        "userName":"dru795"
    }
    resp = request_tool.post_json(url, json=req)
    print(resp)
    resp_json = resp.json()
    code = resp_json['code']
    print(code)
    message = resp_json['message']
    assert   message =='登录成功'
