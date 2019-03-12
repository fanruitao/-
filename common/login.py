import requests
import os
import re
from common.readConfig import ReadConfig
pwd = os.path.dirname(os.getcwd())
config_file = os.path.join(pwd, "common\config.ini")
from common.logger import L

def login():
    path="/uac/auth/form"
    config=ReadConfig(config_file)
    url = config.get_baseurl()
    optocal = config.get_protocol()
    username=config.get_login()[0]
    password=config.get_login()[1]
    data = {'username': username, "password": password}
    httpurl = optocal + "://" + url + path
    head = {}
    head['Content-Type'] = 'application/x-www-form-urlencoded'
    head['Authorization'] = "Basic cGFhc2Nsb3VkLWNsaWVudC11YWM6cGFhc2Nsb3VkQ2xpZW50U2VjcmV0"
    r = requests.post(httpurl, data=data, headers=head)
    result = r.json()
    token=''
    print(result)
    if result['code']!=200:
        print("登录失败")
    else :
        print("登录成功")
        token = re.search(r"'access_token': '(.+?)'", str(result)).group(1)
    return token

