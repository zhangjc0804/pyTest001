from tools.api import request_tool
import pytest
import allure
ids = ['正确数据',
       '用户名错误',
       '密码错误']

cases = [('123zjc', '123456zjc', 2000),
         ('yujl471', 'Jg82SqEi', 9999),
         ('yujl47', 'Jg82SqEi1', 9999)]
@pytest.mark.parametrize('name,pwd,assertion', cases, ids=ids)
@allure.title("批量登录用户")
def test_login(name, pwd, assertion):
    url = 'http://qa.yansl.com:8084/login'
    req = {
        "pwd": pwd,
        "userName": name
    }
    resp = request_tool.post_json(url, json=req)
    print(resp)
    resp_json = resp.json()
    code = resp_json['code']
    print(code)
    data = resp_json['data']
    assert code == assertion

