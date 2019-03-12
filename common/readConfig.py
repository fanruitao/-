
import configparser
import os




class ReadConfig(object):
    def __init__(self,config_file):
        self.cf=configparser.ConfigParser()
        self.cf.read(config_file)
    def get_protocol(self):
        protocol=self.cf.get('HTTP','protocol')
        return protocol
    def get_baseurl(self):
        baseurl=self.cf.get('HTTP','baseurl')
        return baseurl
    def get_logpath(self):
        logpath=self.cf.get('log','logpath')
        return logpath
    def get_login(self):
        username=self.cf.get('login','user')
        password=self.cf.get('login','password')
        return username,password










