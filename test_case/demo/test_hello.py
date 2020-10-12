# -*- coding:utf-8 -*-                                                                                        
# Author : 小吴老师                                                                                           
# Data ：2019/7/18 19:23                                                                                      
import allure
import json                                                                                                   
                                                                                                              
                                                                                                              
@allure.epic('一级归类')                                                                                      
@allure.feature('二级归类')                                                                                   
@allure.story('三级归类')                                                                                     
def test_hello_world():
    allure.attach('http://localhost:8080/demo/login.action', '地址', allure.attachment_type.TEXT)
    print('hello world !')                                                                                    
    request = {                                                                                               
        'pwd': 'a123456',                                                                                     
        'userName': '13s32'                                                                                   
    }                                                                                                         
    allure.attach(json.dumps(request,ensure_ascii=False,indent=4), '请求', allure.attachment_type.TEXT)       
                                                                                                              
    response = {                                                                                              
        'code': 2000,                                                                                         
        'message': '登录成功',                                                                                
        'test_file': {
            'token': 'eyJ0aW1lT3V0IjoxNTYzNDUxMjg4MjY3LCJ1c2VySWQiOjQwMywidXNlck5hbWUiOiIxM3MzMiJ9',          
            'userName': '13s32'                                                                               
        }                                                                                                     
    }                                                                                                         
    allure.attach(json.dumps(response,ensure_ascii=False,indent=4), '响应', allure.attachment_type.TEXT)      
