# -*- coding:utf-8 -*-																		
# Author : 小吴老师                                                                        
# Data ：2019/7/12 7:41                                                                    
from tools.os import shell_tool
import pytest

if __name__ == '__main__':
     # 修改成要执行的测试用例
     test_case1 = './test_case/User/test_sign.py'
     test_case2 = './test_case/User/test_login.py'
     test_case3 = './test_case/User/test_realname.py'
     test_case4 = './test_case/User/test_oldpwd.py'
     test_case5 = './test_case/User/test_changepwd.py'

     xml_report_path = './report/xml/'
     html_report_path = './report/html/'

     pytest.main(['-s', '-q', '--alluredir',
	      xml_report_path, test_case1, test_case2, test_case3, test_case4, test_case5])
     cmd1 = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
     cmd2 = 'allure serve %s' % (xml_report_path)
     shell_tool.invoke(cmd1)
     shell_tool.invoke(cmd2)
