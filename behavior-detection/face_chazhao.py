# encoding:utf-8
import base64
import urllib
import urllib.request as urllib2

import sys
import ssl
from urllib import request,parse

import json

# http://ai.baidu.com/docs#/Face-Python-SDK/6cf546d8

# https://console.bce.baidu.com/ai/#/ai/face/facelib/userList~appId=65991&groupId=hackathon2019&pageNo=1

def chazhao_face(myname):	
    client_id_face = 'e2crS4fE4cfgn2hswCQHjHTA'
    client_secret_face = 'AIsQHpt1CEX3gpEDmPrpO9Oif0TsFOUO'
    host_face = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(client_id_face,client_secret_face)
    req_face = request.Request(host_face)
    req_face.add_header('Content-Type', 'application/json; charset=UTF-8')
    response_face = request.urlopen(req_face)
    #获得请求结果
    content_face = response_face.read()
    #结果转化为字符
    content_face = bytes.decode(content_face)
    #转化为字典
    content_face = eval(content_face[:-1])
    face_access_token = content_face['access_token']
 	
    request_url_face = "https://aip.baidubce.com/rest/2.0/face/v2/identify"
    filename_face = myname+'.jpg'
    f_face = open(filename_face, 'rb')
    img1_face = base64.b64encode(f_face.read())

    params_face = {"face_top_num":"1","group_id":"hackathon2019","images":img1_face,"user_top_num":"1"}
    params_face = urllib.parse.urlencode(params_face)
    request_url_face = request_url_face + "?access_token=" + face_access_token
    request_face = urllib.request.Request(url=request_url_face, data=params_face.encode(encoding='UTF8'))
    request_face.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    response_face = urllib2.urlopen(request_face)
    content_face = response_face.read()
    #print(content_face)
    #b'{"log_id":4245151413,"result_num":1,"result":[{"uid":"caixin","user_info":"caixin","scores":[92.220230102539],"group_id":"hackathon2019"}]}'
    # {'log_id': 2309224473, 'error_msg': 'face not found', 'error_code': 216402}
    content_a_face=json.loads(content_face) 
    print(content_a_face["result"])

    try:
        #正常的操作
        thename = content_a_face["result"][0]["uid"]
    except:
        #发生异常，执行这块代码
        thename = "无人用户"
    else:
        #如果没有异常执行这块代码	
        thename = content_a_face["result"][0]["uid"]
        thescores = content_a_face["result"][0]["scores"]
        print(thescores[0])
        if int(thescores[0]) < 60:  #小于60分 就不认为是这张脸
            thename = "未授权用户"	
			
    print(thename)
	
    if thename == 'caixin':
        thename_cn = "蔡欣 "
    elif thename == 'jiningning':
        thename_cn = "纪宁宁 "
    elif thename == 'zhuwenmin':
        thename_cn = "朱文敏 "
    elif thename == 'zhangweijie':
        thename_cn = "张伟杰 "		
    elif thename == 'shenzhaobin':
        thename_cn = "申兆斌 "
    elif thename == 'pw1_adaxiao':
        thename_cn = "评委 肖紫闻 "
    elif thename == 'pw2_zhongwenbin':
        thename_cn = "评委 钟文斌 "
    elif thename == 'pw3_tangyi':
        thename_cn = "评委 唐弈 "		
    elif thename == 'pw4_yuwenbo':
        thename_cn = "评委 余文波 "
    elif thename == 'pw5_mikael_elley':
        thename_cn = "评委 Mikael_Elley "
    elif thename == 'pw6_zhaozilong':
        thename_cn = "评委 赵子龙 "
    elif thename == 'pw7_baishuo':
        thename_cn = "评委 白硕 "		
    elif thename == 'pw8_guohaoyun':
        thename_cn = "评委 郭浩贇 "
    else:
        thename_cn = "未授权用户"
    return thename_cn



thename_cn_p = chazhao_face("capture")

print(thename_cn_p)
	
		
	
	
	
	
	