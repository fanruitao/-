import unittest
import requests
import re
from common.readConfig import ReadConfig
from common.readCase import *
from common.logger import L
import time
import HTMLTestRunner
import os,sys
from common.configHttp import ConfigHttp
from common.login import login
pwd = os.path.dirname(os.getcwd())

case_file=os.path.join(pwd, "common\\testcase.xlsx")


class UserInfo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.token=add_token()
    def setUp(self):
        pass
    def test_get_userinfo1(self):
        "登录后获取用户信息"
        casename = sys._getframe().f_code.co_name
        L.build_start_line(casename)
        case = ReadCase('userinfo', 'get_userinfo1', case_file).read_case_info()
        confighttp = ConfigHttp(*case[0])
        response = confighttp.get(self.token)
        result = response.json()
        print(result)
    def test_get_userinfo2(self):
        "登录后，修改用户信息"
        casename = sys._getframe().f_code.co_name
        L.build_start_line(casename)
        case = ReadCase('userinfo', 'get_userinfo2', case_file).read_case_info()
        print(case)
        confighttp = ConfigHttp(*case[0])
        response = confighttp.put(self.token)
        result = response.json()
        print(result)







    def tearDown(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(UserInfo('test_get_userinfo1'))
    suite.addTest(UserInfo('test_get_userinfo2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # if not os.path.exists('./result'):
    #     os.makedirs('./result')
    # filename = r'./result/' + now + '_result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"app接口测试", description=u"用例执行情况:")
    # runner.run(suite)
    # fp.close()
