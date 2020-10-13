from tools.api import request_tool
from tools.data import random_tool
from tools.data import identity_tool
import allure
@allure.title("实名认证")
def test_realname(token):
    headers = {
        'token': token,
        'charset': 'UTF-8'
    }
    url = 'http://qa.yansl.com:8084/cst/realname2'
    email = random_tool.random_email()
    sex = random_tool.random_sex()  # 随机生成男(1)或女(0)
    cst_name = random_tool.random_name(sex)
    area = random_tool.random_area()
    area_id = area['code']
    area_name = area['name']
    province = area['province']
    city = area['city']
    birth_days = random_tool.random_birthday(18, 35)
    cert_no = identity_tool.generate_id(sex=sex, area_id=area_id, birth_days=birth_days)
    req ={
              "cstId": 15790,
              "customerInfo": {
                   "birthday": '2020-10-31',
                   "certno": cert_no,
                   "city":  city,
                   "cstName": cst_name,
                   "email":email,
                   "province": province,
                   "sex": sex
              }
               }
    print(req)
    resp = request_tool.post_json(url=url,headers=headers, json=req)
    resp_json = resp.json()
    message=resp_json['message']
    assert message =="认证成功"
