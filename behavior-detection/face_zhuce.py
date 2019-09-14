# encoding:utf-8
import base64
import urllib
import urllib.request as urllib2

import sys
import ssl
from urllib import request,parse

import time

# client_id 为官网获取的AK， client_secret 为官网获取的SK
#获取token
def get_token():
    client_id = 'e2crS4fE4cfgn2hswCQHjHTA'
    client_secret = 'AIsQHpt1CEX3gpEDmPrpO9Oif0TsFOUO'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(client_id,client_secret)
    req = request.Request(host)
    req.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = request.urlopen(req)
    #获得请求结果
    content = response.read()
    #结果转化为字符
    content = bytes.decode(content)
    #转化为字典
    content = eval(content[:-1])
    return content['access_token']
 

face_access_token = get_token()
print(face_access_token)


'''
人脸注册
'''

def zhuce(myname):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/add"
    filename = myname+'.jpg'
    f = open(filename, 'rb')
    # 参数images：图像base64编码
    img1 = base64.b64encode(f.read())
    # 二进制方式打开图文件
    
    params = {"group_id":"hackathon2019","images":img1,"uid":myname,"user_info":myname}
    params = urllib.parse.urlencode(params)
    request_url = request_url + "?access_token=" + face_access_token
    request = urllib.request.Request(url=request_url, data=params.encode(encoding='UTF8'))
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        print(content)
    time.sleep(60)
zhuce('pw1_adaxiao')
zhuce('pw2_zhongwenbin')
zhuce('pw3_tangyi')	
zhuce('pw4_yuwenbo')	
zhuce('pw5_mikael-elley')
zhuce('pw6_zhaozilong')	
zhuce('pw7_baishuo')
zhuce('pw8_guohaoyun')	
	
	
	