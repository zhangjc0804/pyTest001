from tools.api import request_tool
import allure

from tools.report import assert_tool
@allure.epic('guoyasoft.com')
@allure.feature('用户模块')
@allure.story('修改密码接口')
@allure.title("修改密码成功")
def test_changepwd(token):
     url = 'qa.yansl.com:8084/user/changepwd'
     headers = {
          'token': token,
          'charset': 'UTF-8'
     }
     req = {
          "newPwd": "123456zjc",
          "oldPwd": "123456zjcq",
          "reNewPwd": "123456zjc",
          "userName": "dru795"
     }
     resp = request_tool.post_json(url=url, headers=headers, json=req)
     resp_json = resp.json()
     # 提取响应内容进行断言；验证是否修改成功；
     #message = resp_json['message']
     #assert  message == "修改成功1"
     allure.attach("预期结果:{},实际结果：{}".format(200,resp.status_code),"响应状态码",allure.attachment_type.TEXT);
     assert_tool.assert_equal(resp.status_code,200)

