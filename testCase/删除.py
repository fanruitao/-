
import requests
import re
import time
loginurl="http://180.168.116.54:260/uac/auth/form"
url='http://uat.iotbull.com:260/pdc/v1/products/type/base'

head={}
head['Content-Type']='application/x-www-form-urlencoded'
head['Authorization']="Basic cGFhc2Nsb3VkLWNsaWVudC11YWM6cGFhc2Nsb3VkQ2xpZW50U2VjcmV0"
data={'username':"18221629114","password":"333333"}
r=requests.post(loginurl,data=data,headers=head)
result=r.json()
token=re.search(r"'access_token': '(.+?)'",str(result)).group(1)
print(token)

def deleteProduct():
    print("************开始删除产品*************")
    head1={}
    head1['Content-Type']='application/json'
    head1['Authorization']='Bearer '+token
    print('head1',head1)

    param={'pageNum':1,'pageSize':500}

    r1=requests.get(url,params=param,headers=head1)
    result2=r1.json()
    print(result2)
    t=re.findall("'productId': '(.+?)'",str(result2))
    print(t)

    # for i in range(0,len(t)):
    for i in t:
        print('i',i)
        time1=time.time()

        head1 = {}
        head1['Content-Type'] = 'application/json'
        head1['Authorization'] = 'Bearer ' + token

        url2='http://uat.iotbull.com:260/pdc/v1/products/%s/' %i
        requests.delete(url2,headers=head1)
        time2=time.time()
        print(time2-time1)

def deleteCategory():
    print("##############开始删除品类####################")
    url="http://uat.iotbull.com:260/pdc/v1/prdcategories/tree"
    head1 = {}
    head1['Content-Type'] = 'application/json'
    head1['Authorization'] = 'Bearer ' + token
    r=requests.get(url,headers=head1)
    print(str(r.json()))

    g = re.findall("'cid': '(.+?)', 'name': '.+?', 'parentId': None, 'children'", str(r.json()))
    print(g)
    print("长度是：%s",len(g))
    for j in g:
        print('j', j)
        time1 = time.time()

        head2 = {}
        head2['Content-Type'] = 'application/json'
        head2['Authorization'] = 'Bearer ' + token

        url2 = 'http://uat.iotbull.com:260/pdc/v1/prdcategories/%s/' % j
        requests.delete(url2, headers=head1)
        time2 = time.time()
        print(time2 - time1)
deleteProduct()
deleteCategory()







