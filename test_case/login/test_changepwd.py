from tools.api import request_tool
import pytest
def test_changepwd(token):
     url= 'http://qa.yansl.com:8084/user/changepwd'
     headers = {
          'token': token,
          'charset': 'UTF-8'
     }
     req={
  	"newPwd": "123456zjc",
  	"oldPwd": "123456zjcq",
  	"reNewPwd": "123456zjc",
  	"userName": "dru795"
}
     resp = request_tool.post_json(url=url,headers=headers, json=req)
     resp_json = resp.json()
     message = resp_json['message']
     assert message == "修改成功1"
