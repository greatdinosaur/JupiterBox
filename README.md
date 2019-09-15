# JupiterBox
——The Equipment for Storage of Driving Evidence on Blockchain
```
驾驶行为数据存证装置
Team Jupiter（蔡欣  张伟杰  申兆斌  朱文敏  纪宁宁）
2019-09-15
WanXiang Blockchain Hackathon @ ShangHai
```

###文件（运行环境Ubuntu18.04，python3.7）
```
run_backward.py
run_backward_on_pi_new.py(raspberry pi version)
```

###流程思路：
1.从摄像头截图，得到capture.jpg
2.将capture.jpg送给百度云进行人脸识别，检测驾驶员是否有驾驶权限
3.将capture.jpg送给百度云进行驾驶行为检测（未来正式的产品应当是在本地进行边缘推理）。
4.对驾驶行为结果进行判断：若正常，则图片哈希值上链；若异常，则
   1.用给图片加字的方式，把驾驶行为检测的异常结果加在capture.jpg上；
   2.复制图片到pic_out_law文件夹，并且图片网址上链（当然在demo中是localhost）。
5.在PyQt5构建的界面中实时显示图片（含图片上的异常驾驶行为文字）。
6.运行python3 run_backward.py，开启上述（1）至（5）自动循环，间隙时间可设置为3秒。
7.可通过web界面查看

###主要函数：
record()-------------从摄像头截图函数
jsongo()-------------百度云获得access_key，然后进行图片驾驶行为检测，获得json结果
jiazi()--------------给图片加上文字
showpic()------------用PyQt5实时显示图像
get_hash()-----------获得文件的哈希值
face_zhuce()---------注册人脸
face_chazhao()-------查找人脸，用于检测驾驶员是否有车辆权限
tochain()--------------数据记录上链