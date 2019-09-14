# encoding:utf-8

import urllib, sys
import urllib.request as urllib2
import ssl

import time

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2TwF6IgFjENcjXQjAfGNGH2e&client_secret=NqazPvZLaQuMynwQvghZFtMisMAxP8A7'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
'''
if (content):
    print(content)
'''


import base64
import json

'''
驾驶行为分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/driver_behavior"

# 二进制方式打开图片文件
f = open('capture.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}

params = urllib.parse.urlencode(params)


content=json.loads(content) 

access_token = content["access_token"]
request_url = request_url + "?access_token=" + access_token
#request = urllib.request.Request(url=request_url, data=urllib.parse.urlencode(params).encode(encoding='UTF8'))
request = urllib.request.Request(url=request_url, data=params.encode(encoding='UTF8'))
request.add_header('Content-Type', 'application/x-www-form-urlencoded')

response = urllib2.urlopen(request)
content = response.read()
if content:

    #content = str(content).replace("b","")
    content=json.loads(content) 
    print(content)
    cellphone_threshold = content["person_info"][0]["attributes"]["cellphone"]["threshold"]
    cellphone_score     = content["person_info"][0]["attributes"]["cellphone"]["score"]
    both_hands_leaving_wheel_threshold = content["person_info"][0]["attributes"]["both_hands_leaving_wheel"]["threshold"]
    both_hands_leaving_wheel_score     = content["person_info"][0]["attributes"]["both_hands_leaving_wheel"]["score"]
    not_facing_front_threshold = content["person_info"][0]["attributes"]["not_facing_front"]["threshold"]
    not_facing_front_score     = content["person_info"][0]["attributes"]["not_facing_front"]["score"]
    not_buckling_up_threshold = content["person_info"][0]["attributes"]["not_buckling_up"]["threshold"]
    not_buckling_up_score     = content["person_info"][0]["attributes"]["not_buckling_up"]["score"]
    smoke_threshold = content["person_info"][0]["attributes"]["smoke"]["threshold"]
    smoke_score     = content["person_info"][0]["attributes"]["smoke"]["score"]	
	
	
	
	
    is_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    is_out_law = is_time+" "
    if cellphone_score > cellphone_threshold :
        is_out_law = is_out_law + "开车玩手机 "
    if both_hands_leaving_wheel_score > both_hands_leaving_wheel_threshold :
        is_out_law = is_out_law + "双手离开方向盘 "
    if not_facing_front_score > not_facing_front_threshold :
        is_out_law = is_out_law + "目光未看前方 "	
    if not_buckling_up_score > not_buckling_up_threshold :
        is_out_law = is_out_law + "未系安全带 "	
    if smoke_score > smoke_threshold :
        is_out_law = is_out_law + "吸烟 "	

		
    print(is_out_law)	
		
		
'''
{
    'person_num': 1,
    'person_info': [
        {
            'attributes': {
                'cellphone': {
                    'threshold': 0.6380000114440918,
                    'score': 0.2699644267559052
                },
                'both_hands_leaving_wheel': {
                    'threshold': 0.4909999966621399,
                    'score': 0.002107238164171576
                },
                'not_facing_front': {
                    'threshold': 0.4580000042915344,
                    'score': 0.5735644102096558
                },
                'not_buckling_up': {
                    'threshold': 0.4490000009536743,
                    'score': 0.06196397915482521
                },
                'smoke': {
                    'threshold': 0.4370000064373016,
                    'score': 0.08515523374080658
                }
            },
            'location': {
                'width': 539,
                'top': 138,
                'height': 341,
                'left': 39
            }
        }
    ],
    'log_id': 6735469132374043336
}
'''
	
	
	