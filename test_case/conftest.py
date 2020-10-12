import pytest
import random

from datetime import datetime
from dateutil.relativedelta import relativedelta

from tools.api import request_tool


@pytest.fixture(scope='session')                            
def pub_dic():                                              
    data = {'token':'asdfasdfjsldkfjlsxllkj'}               
    return data                                             


@pytest.fixture(scope='session')                            
def pub_list():                                             
    data = ['张三','zhangsan',30,'男','aaa123']             
    return data                                             


@pytest.fixture(scope='session')                            
def pub_var():                                              
    token = 'xxxxsdfsdfjkllwklewe'                          
    return token

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

@pytest.fixture(scope='session')
def birthday(min=80,max=100):
    age=random.randint(min,max)
   # print(str(age)+'岁')
    today=datetime.now()
    birth_days = datetime.strftime(today - relativedelta(years=age), "%Y-%m-%d")
    birth_days=datetime.strptime(birth_days, '%Y-%m-%d')
    print(birth_days)
    return birth_days
