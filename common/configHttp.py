import requests
import os
from common.readConfig import ReadConfig
pwd = os.path.dirname(os.getcwd())
config_file = os.path.join(pwd, "common\config.ini")
from common.logger import L
class ConfigHttp:

    def __init__(self,*caseinfo):

        self.casename = caseinfo[0]
        self.method=caseinfo[1]
        self.path=caseinfo[2]
        self.headers=caseinfo[3]
        self.data=caseinfo[4]
        self.result=caseinfo[5]
        self.code=caseinfo[6]
        self.msg=caseinfo[7]
        self.des=caseinfo[8]


    def set_url(self):
        self.url = ReadConfig(config_file).get_baseurl()
        self.optocal = ReadConfig(config_file).get_protocol()
        self.httpurl = self.optocal + "://" + self.url+self.path
        return self.httpurl
    def set_header(self,token):
        t=''
        if "'Authorization':''" in self.headers:
            t=self.headers.replace("'Authorization':''","'Authorization':'Bearer  %s'"% token)
            return t
        else:
            print("#########")
            return self.headers

    def get(self,token):
        url=self.set_url()
        headers = eval(self.set_header(token))
        print(headers)
        response = requests.get(url, headers=headers, params=self.data)
        return response


    def post(self,token):
        url = self.set_url()
        headers = eval(self.set_header(token))
        response = requests.post(url, headers=headers,  data=self.data)
        return response
    def put(self,token):
        url = self.set_url()
        headers = eval(self.set_header(token))
        response = requests.put(url, headers=headers,  data=self.data)
        return response

