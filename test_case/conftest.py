import pytest
from tools.api import request_tool
@pytest.fixture(scope='session')
def token():
    url='http://qa.yansl.com:8084/login'
    req={
         "pwd": "123456zjc",
         "userName": "123zjc"
        }
    resp = request_tool.post_json(url, json=req)
    print(resp)
    resp_json=resp.json()
    token = resp_json['data']['token']
    print(token)
    return token


