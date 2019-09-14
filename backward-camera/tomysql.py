#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''

import pymysql
 
# 打开数据库连接
db = pymysql.connect("mysql.rdsm7htgcrx38if.rds.bj.baidubce.com","hackathon2019","hackathon2019","hackathon2019" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()

'''

# https://www.runoob.com/python3/python-mysql-connector.html

import mysql.connector
 
mydb = mysql.connector.connect(
  host="mysql.rdsm7htgcrx38if.rds.bj.baidubce.com",
  user="hackathon2019",
  passwd="hackathon2019",
  database="hackathon2019"
)
mycursor = mydb.cursor()

# sql = "INSERT INTO `backward-camera` (`theID`, `thename`, `theContent`, `theTime`, `theLaw`, `theHash`, `theURL`) VALUES (NULL, '11', '222', '333', '', '444', '555')"
sql = "INSERT INTO `backward-camera` (`thename`, `theContent`, `theTime`, `theLaw`, `theHash`, `theURL`) VALUES ('名字', '内容', '2019-09-11 18：22：12', '合法', 'hashhash4', '555urlurl')"

mycursor.execute(sql)
 
mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
print(mycursor.rowcount, "记录插入成功。")



