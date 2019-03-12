import unittest
import requests
import re
import time
import HTMLTestRunner
import os

class FindAllDevice(unittest.TestCase):
    '''查询所有设备列表'''
    def setUp(self):
        self.url='http://172.16.135.158:8030/v1/devices/findAll'
    def get_product_id(self):
        r=requests.get(self.url)
        result=r.json()
        productuuid=re.findall(r"\{'productUUID': '(\d+)', 'serielNo': '(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})',",str(result))
        deviceuuid = re.findall(r"'deviceUUID': '(\w+)', 'devType'", str(result))
        print(deviceuuid)
        return productuuid
    def get_device_id(self):
        r=requests.get(self.url)
        result=r.json()
        deviceuuid = re.findall(r"'deviceUUID': '(\w+)', 'devType'", str(result))
        return deviceuuid


    def test_get_all_devices(self):
        """查询所有设备列表 v1/devices/findAll """
        r=requests.get(self.url)
        result=r.json()
        print(result)
        productlist=self.get_product_id()
        print((productlist))
        self.assertEqual(result['code'],200)
        self.assertEqual(result['message'],'操作成功')
    def test_get_device_info(self):
        """根据终端 UUDI 查询设备列表信息/v1/devices/{DEVICE_UUID}"""
        deviceuuid=self.get_device_id()[0]
        testurl='http://172.16.135.158:8030/v1/devices/%s' % deviceuuid
        print(testurl)
        r=requests.get(testurl)
        result=r.json()
        print(result)
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '操作成功')

    def test_get_activate_code(self):
        """获取激活码 /products/v1/{productUUID}/devices/{serialNumber}"""
        productlist = self.get_product_id()
        try:
            pruductuuid=productlist[0][0]
            seriel=productlist[0][1]
        except IndexError as e:
            print("数据库中的productid 没有匹配到")
        else:
            testurl='http://172.16.135.158:8030/products/v1/%s/devices/%s' % (pruductuuid,seriel)
            r=requests.get(testurl)
            result=r.json()
            self.assertEqual(result['code'], 10060012)
            self.assertIn('设备已经激活',result['message'])
    def test_query_product_list(self):
        """查询产品列表 /v1/products """
        testurl = 'http://172.16.135.158:8030/v1/products'
        r = requests.get(testurl)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '操作成功')

    def test_get_product_info(self):
        """查询产品信息 /v1/product/{PRODUCT_ID}"""
        productlist = self.get_product_id()
        try:
            pruductuuid = productlist[0][0]
        except IndexError as e:
            print("数据库中的productid 没有匹配到")
        else:

            testurl='http://172.16.135.158:8030/v1/product/%s' % pruductuuid
            r = requests.get(testurl)
            result = r.json()
            print(result)
            self.assertEqual(result['code'], 9999404)
            self.assertEqual(result['message'], '找不到指定资源')
    def test_get_stream_info(self):
        """ 查询数据端点（Stream）列表信息  /v1/device/{deviceId}/streams"""
        deviceuuid = self.get_device_id()[0]
        testurl = 'http://172.16.135.158:8030/v1/device/%s/streams' % deviceuuid
        print(testurl)
        r = requests.get(testurl)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '操作成功')
    def test_add_product(self):
        """新增产品  /v1/product"""
        data={
                  "allowActiveRegister": True,
                  "allowMultiAdmin": True,
                  "createdTime": " ",
                  "creator": "string",
                  "creatorId": 'hello',
                  "database": "string",
                  "delete": True,
                  "description": "string",
                  "id": 0,
                  "key": "string",
                  "lastOperator": "string",
                  "lastOperatorId": 0,
                  "linkType": 0,
                  "name": "string",
                  "productId": "string",
                  "productImageVo": {
                    "icon": "string",
                    "image": "string"
                  },
                  "register": True,
                  "release": True,
                  "tableName": "string",
                  "updateTime": " "
        }
        testurl='http://172.16.135.158:8030/v1/product'
        r=requests.post(testurl,data=data)
        result = r.json()
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '操作成功')

    def test_activate_device(self):
        pass
    def tearDown(self):
        pass

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(TestApp('test_add_gateway'))
    suite.addTest(FindAllDevice('test_get_all_devices'))
    suite.addTest(FindAllDevice('test_get_device_info'))
    suite.addTest(FindAllDevice('test_get_activate_code'))
    suite.addTest(FindAllDevice('test_query_product_list'))
    suite.addTest(FindAllDevice('test_get_product_info'))
    suite.addTest(FindAllDevice('test_get_stream_info'))
    suite.addTest(FindAllDevice('test_add_product'))

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

