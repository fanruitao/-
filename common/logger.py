#coding=utf-8

import logging
import time
import os
from common import readConfig


class logger:
    def  __init__(self,Clevel=logging.DEBUG,Flevel=logging.INFO):
        now = time.strftime("%Y-%m-%d %H_%M_%S")

        if os.path.exists('../log'):
            logpath = '../log/' + now + '.log'
        else:
            os.makedirs('../log')
            logpath = '../log/' + now + '.log'
        print(logpath)

        self.logger=logging.getLogger("接口测试log")
        self.logger.setLevel(logging.DEBUG)
        fmt=logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        ch=logging.StreamHandler()
        ch.setFormatter(fmt)
        ch.setLevel(Clevel)

        fh=logging.FileHandler(logpath)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

    def build_start_line(self,casename):
        self.logger.info("***********************" + casename + " START************************")
    def build_end_line(self,casename):
        self.logger.info("***********************" + casename + " END**************************")
L=logger()
print(L)