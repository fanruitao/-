import unittest
import requests
import re
from common.readConfig import ReadConfig
from common.readCase import ReadCase
from common.logger import L
import time
import HTMLTestRunner
import os,sys
from common.configHttp import ConfigHttp
pwd = os.path.dirname(os.getcwd())

case_file=os.path.join(pwd, "common\\testcase.xlsx")


class LogIn(unittest.TestCase):


    def setUp(self):
        pass
    def test_post_mobile_login1(self):
        "已注册过的手机号码,验证码登录"
        casename = sys._getframe().f_code.co_name
        L.build_start_line(casename)
        case = ReadCase('login', 'post_mobile_login1', case_file).read_case_info()
        print(case[0])
        print(case[1])

        L.info("获取到的用例信息为： %s" % str(case))
        L.info("第一步获取验证码")
        confighttp = ConfigHttp(*case[0])
        response = confighttp.get()
        result = response.json()
        L.info("第一步返回的请求内容为： %s" % str(result))
        L.info("第二步登录")
        # time.sleep(60)
        confighttp2 = ConfigHttp(*case[1])
        response2 = confighttp2.post()
        result2 = response2.json()
        L.info("返回的请求内容为： %s" % str(result2))
        self.assertEqual(result2['code'], 200)
        self.assertIn(case[1][7], result['message'])
        L.build_end_line(casename)
    def test_post_mobile_login2(self):
        "未注册过的手机号码,验证码登录"
        casename = sys._getframe().f_code.co_name
        L.build_start_line(casename)
        case = ReadCase('login', 'post_mobile_login2', case_file).read_case_info()
        print(case[0])
        print(case[1])

        L.info("获取到的用例信息为： %s" % str(case))
        L.info("第一步获取验证码")
        confighttp = ConfigHttp(*case[0])
        response = confighttp.get()
        result = response.json()
        L.info("第一步返回的请求内容为： %s" % str(result))
        L.info("第二步登录")
        # time.sleep(60)
        confighttp2 = ConfigHttp(*case[1])
        response2 = confighttp2.post()
        result2 = response2.json()
        L.info("返回的请求内容为： %s" % str(result2))
        self.assertEqual(result['code'], 901003)
        self.assertIn(case[0][7], result['message'])
        L.build_end_line(casename)
    def post_password_login1(self):
        "已注册过的手机号码，密码登录"
        casename=sys._getframe().f_code.co_name
        L.build_start_line(casename)
        case=ReadCase('login','post_password_login1',case_file).read_case_info()[0]
        L.info("获取到的用例信息为： %s" % str(case))
        confighttp = ConfigHttp(*case)
        response=confighttp.post()
        result=response.json()
        L.info("返回的请求内容为： %s"  % str(result))
        self.assertEqual(result['code'],200)
        self.assertEqual(result['message'], case[7])
        L.build_end_line(casename)
    def post_password_login2(self):
        "已注册过的手机号码，密码填写错误登录"
        casename=sys._getframe().f_code.co_name
        L.build_start_line(casename)
        case=ReadCase('login','post_password_login2',case_file).read_case_info()[0]
        L.info("获取到的用例信息为： %s" % str(case))
        confighttp = ConfigHttp(*case)
        response=confighttp.post()
        result=response.json()
        L.info("返回的请求内容为： %s"  % str(result))
        self.assertEqual(result['code'],500)
        self.assertEqual(result['message'], case[7])
        L.build_end_line(casename)
    def post_password_login3(self):
        "已注册过的手机号码，密码填写错误登录"
        casename=sys._getframe().f_code.co_name
        L.build_start_line(casename)
        case=ReadCase('login','post_password_login3',case_file).read_case_info()[0]
        L.info("获取到的用例信息为： %s" % str(case))
        confighttp = ConfigHttp(*case)
        response=confighttp.post()
        result=response.json()
        L.info("返回的请求内容为： %s"  % str(result))
        self.assertEqual(result['code'],500)
        self.assertEqual(result['message'], case[7])
        L.build_end_line(casename)


    def tearDown(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LogIn('test_post_mobile_login1'))
    suite.addTest(LogIn('test_post_mobile_login2'))
    suite.addTest(LogIn('post_password_login1'))
    suite.addTest(LogIn('post_password_login2'))
    suite.addTest(LogIn('post_password_login3'))




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

