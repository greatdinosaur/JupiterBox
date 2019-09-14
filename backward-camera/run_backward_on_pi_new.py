#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys, pygame
import cv2
import numpy as np

from PIL import Image, ImageDraw, ImageFont

import urllib, sys
import urllib.request as urllib2
import ssl
import base64
import json
import os
import binascii
import hashlib


from urllib import request,parse

import mysql.connector 
mydb = mysql.connector.connect(
host="mysql.rdsm7htgcrx38if.rds.bj.baidubce.com",
user="hackathon2019",
passwd="hackathon2019",
database="hackathon2019"
)
mycursor = mydb.cursor()


def get_file_md5(file_path):
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).upper()


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
content=json.loads(content) 
access_token = content["access_token"]




def gen_img(size=None):
    if size is None:
        size = 400
        #生成大小为400x400RGBA是四通道图像，RGB表示R，G，B三通道，A表示Alpha的色彩空間
    image = Image.new(mode='RGBA', size=(400, 400), color=(255, 55, 55))
    # ImageDraw.Draw 简单平面绘图
    draw_table = ImageDraw.Draw(im=image)
    # 直接显示图片
    image.show()

def pic_open(filepath):
    #图片打开与显示
    image = Image.open(filepath)
    return image
        
def get_size(image):
    #获取图像的宽和高
    width, height = image.size
    return width,heitht

def pic_text(filepath,size,text,setFont,fillColor,filename,direction=None):
    #print(filepath,size,text,setFont,fillColor)
    #打开图片
    image=pic_open(filepath)
    #新建绘图对象
    draw = ImageDraw.Draw(image)
    #显示图片
    #image.show()
    draw.text((40,40),text,font=setFont,fill=fillColor,direction=None)
    #image.show()
    #保存
    pic_save(image,filename)
    
def pic_save(image,filename):
    #保存
    image.save(filename)    
        


#截图函数
'''
def snapShotCt(camera_idx = 0):# camera_idx default = 0 normally usb = 1 /or you can try with 1,2,3
    cap = cv2.VideoCapture(camera_idx)
    # get a frame
    ret, frame = cap.read()
 
    while ret: 
        cv2.imwrite("./capture.jpg", frame) # write picture 
        time.sleep(0) # delay 1s, delete if possible
        ret, frame = cap.read() # next frame
        break # for test, delete in real use
    cap.release()
'''

#旋转图像的函数 树莓派专用 PC不用 因为它的摄像头方向
def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    #return cv2.warpAffine(image, M, (nW, nH))
    return cv2.warpAffine(image, M, (nW, nH),borderValue=(255,255,255))

def snapShotCt(camera_idx = 0):# camera_idx default = 0 normally usb = 1 /or you can try with 1,2,3
    #os.system('raspistill -o capture.jpg -t 1000 -w 300 -h 600 -n')  # 全屏
    os.system('raspistill -o capture.jpg -t 1000 -w 300 -h 300 -n') 

    img0 = cv2.imread("capture.jpg")
    imgRotation = rotate_bound(img0, 270)
    cv2.imwrite("capture.jpg",imgRotation, [int( cv2.IMWRITE_JPEG_QUALITY), 100]) # 默认95


	
#人脸查找函数
def chazhao_face(myname):	
    import urllib
    #import urllib.request as urllib2
    from urllib import request,parse
	
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
    #print(content_a_face)

    try:
        #正常的操作
        thename = content_a_face["result"][0]["uid"]
    except:
        #发生异常，执行这块代码
        thename = "无人"
    else:
        #如果没有异常执行这块代码	
        thename = content_a_face["result"][0]["uid"]
        thescores = content_a_face["result"][0]["scores"]
        print(thescores[0])
        if int(thescores[0]) < 60:  #小于60分 就不认为是这张脸
            thename = "未授权用户"	
			
    #print(thename)
	
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


	
	
	
	

pygame.init()

#抓取频率，抓取一次
SLEEP_TIME_LONG = 0

size = width, height = 300, 300
speed = [2, 2]
black = 0, 0, 0

pygame.display.set_caption('视频窗口@dyx1024') 
screen = pygame.display.set_mode(size)

while True:
    #截图
    snapShotCt()

    #开始给图片加上字
    size=None
    #gen_img()
        
    #** ImageFont模块**
    #选择文字字体和大小
    setFont = ImageFont.truetype('Dengl.ttf', 16)
    #设置文字颜色
    fillColor = "#0000ff"   #蓝色
    #text="哈哈"+content
    size=(10,10)
    filepath="capture.jpg"
    filename="capture.jpg"	

    '''
    驾驶行为分析
    '''
    
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/driver_behavior"
    
    # 二进制方式打开图片文件
    f = open('capture.jpg', 'rb')
    img = base64.b64encode(f.read())
    
    params = {"image":img}
    
    params = urllib.parse.urlencode(params)
    

    request_url = request_url + "?access_token=" + access_token
    #request = urllib.request.Request(url=request_url, data=urllib.parse.urlencode(params).encode(encoding='UTF8'))
    request = urllib.request.Request(url=request_url, data=params.encode(encoding='UTF8'))
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')

    is_out_law = ""
	
    response = urllib2.urlopen(request)
    content_r = response.read()
    if content_r:
        #print(content_r)
        content_a=json.loads(content_r) 
        #print(str(content_a))
        #print(content_a)
        if content_a["person_num"]!=0:
            #有人才有检测  无人不检测
            cellphone_threshold = content_a["person_info"][0]["attributes"]["cellphone"]["threshold"]
            cellphone_score     = content_a["person_info"][0]["attributes"]["cellphone"]["score"]
            both_hands_leaving_wheel_threshold = content_a["person_info"][0]["attributes"]["both_hands_leaving_wheel"]["threshold"]
            both_hands_leaving_wheel_score     = content_a["person_info"][0]["attributes"]["both_hands_leaving_wheel"]["score"]
            not_facing_front_threshold = content_a["person_info"][0]["attributes"]["not_facing_front"]["threshold"]
            not_facing_front_score     = content_a["person_info"][0]["attributes"]["not_facing_front"]["score"]
            not_buckling_up_threshold = content_a["person_info"][0]["attributes"]["not_buckling_up"]["threshold"]
            not_buckling_up_score     = content_a["person_info"][0]["attributes"]["not_buckling_up"]["score"]
            smoke_threshold = content_a["person_info"][0]["attributes"]["smoke"]["threshold"]
            smoke_score     = content_a["person_info"][0]["attributes"]["smoke"]["score"]	
	
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
            #print(is_out_law)				


    is_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if is_out_law == "":  #没有违法行为
        is_out_law = is_time
        theLaw = "合法"
    else:  # 存在违法行为
        theLaw = "违法"
        is_out_law = is_time + " " + is_out_law

    thename_cn_p = chazhao_face("capture")
    mytext = thename_cn_p + is_out_law
    print(mytext)		
	
    #打开图片
    image=pic_open(filepath)
    #添加文字
    pic_text(filepath,size,mytext,setFont,fillColor,filename,direction=None)

    time.sleep(0)	
	
    if is_out_law != is_time: #存在违法 才保存
        savetobkfile = str(time.time())+".jpg"
        savetobkpath = "/var/www/html/"+savetobkfile
        savetobkurl = "http://192.168.1.111/"+savetobkfile
        pic_text(filepath,size,mytext,setFont,fillColor,savetobkpath,direction=None)
        #违法的图片 还要单独保存一次	
        #明文（图片链接）上链
        the_pic_hash = get_file_md5("capture.jpg")
        st16 = mytext+'URL: '+savetobkurl+' Hash:'+	the_pic_hash
        #
        #
    else:	# 合法情况 不保存图片
        #哈希值上链
        the_pic_hash = get_file_md5("capture.jpg")
        print(the_pic_hash)	
        #哈希值上链
        st16 = mytext+'无违法行为 hash: '+the_pic_hash

    #print(st16)
    # 把字符串s编码成unicode
    st16 = binascii.b2a_hex(st16.encode('utf-8'))  # 字符串转16进制
    st16 = str(st16).replace("b'","").replace("'","")
    #print(st16)
		
    toruncmd = 'cita-cli store data --content 0x'+st16+' --private-key 0x5f0258a4778057a8a7d97809bd209055b2fbafa654ce7d31ec7191066b9225e6 --url http://121.196.200.225:1337'
    reslt = os.popen(toruncmd).readlines() 
    #这个返回值是一个list
		
    reslt = str(reslt).replace("\\n', '","")
    reslt = str(reslt).replace("\\n'","")
    reslt = str(reslt).replace("'","")
    #print(reslt)
    contnt=json.loads(reslt) 
    #print(str(reslt))
    the_tx_hash = str(contnt[0]["result"]["hash"])
    the_tx_url = "https://microscope.citahub.com/#/transaction/hash/"+the_tx_hash
    print(the_tx_url)

	
    thename = thename_cn_p  #驾驶员名字
    theContent = "车内摄像头"
    theTime  = is_time
    theLaw = theLaw
    theHash = the_pic_hash
    theURL = the_tx_url	
	
    # 写入mysql
    # https://www.runoob.com/python3/python-mysql-connector.html
    #sql = "INSERT INTO `backward-camera` (`theID`, `thename`, `theContent`, `theTime`, `theLaw`, `theHash`, `theURL`) VALUES (NULL, '11','11', '222', '333', '444', '4e4')"
    sql = "INSERT INTO `backward-camera` (`thename`, `theContent`, `theTime`, `theLaw`, `theHash`, `theURL`) VALUES ('"+thename+"', '"+theContent+"', '"+theTime+"', '"+theLaw+"', '"+theHash+"', '"+theURL+"')"
    #print(sql)
    mycursor.execute(sql)
    mydb.commit() # 数据表内容有更新，必须使用到该语句
    #print(mycursor.rowcount, "记录插入成功。")
		
		
	#加载图像
    image = pygame.image.load('capture.jpg')

    #传送画面
    screen.blit(image, speed)

    #显示图像
    pygame.display.flip()

    #休眠一下，等待
    time.sleep(SLEEP_TIME_LONG)
    print("  ")
    

	
	
	
	