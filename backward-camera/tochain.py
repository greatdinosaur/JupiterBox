#!/usr/bin/python3
# -*- coding: utf-8 -*-


s = "2019-09-09 01:44:23无违法行为 hash: 9A7F44357CA070E502A35174BA3D307F"
# 把字符串s编码成unicode


import binascii
str_16 = binascii.b2a_hex(s.encode('utf-8'))  # 字符串转16进制
print(str(str_16).replace("b'","").replace("'",""))
# http://www.bejson.com/convert/ox2str/


'''
st16 = str(s.encode('utf-8'))
st16 = st16.replace("\\x", "")
st16 = st16.replace("b\'", "")
st16 = st16.replace("\'", "")
print(st16)
'''

'''
# content以0x开头，后面是UTF-8转十六进制的文本
# cita-cli store data --content 0xe4b8ade59bbde4baba --private-key 0x5f0258a4778057a8a7d97809bd209055b2fbafa654ce7d31ec7191066b9225e6 --url http://121.196.200.225:1337

import os
import json

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

'''



