# -*- coding: UTF-8 -*
# 列表 List
# import ptvsd
# ptvsd.enable_attach(address =('0.0.0.0',8889))
# ptvsd.wait_for_attach()

mydata=['高兴',"生气","郁闷","可爱"]
print(mydata)

# len 得到列表内数据项个数
print(len(mydata))

# append 尾部添加一项
mydata.append("Append")
print(mydata)

# pop 删除尾部项

mydata.pop()
print(mydata)

# extend 列表添加到尾部
b=["苹果",'橘子',"香蕉"]
mydata.extend(b)
print(mydata)

# remove 移除指定列表
mydata.remove("苹果")
print(mydata)

# insert 在指定位置添加项
mydata.insert(1,'飞机')
print(mydata)

# 判断对象是否是list类型
print(isinstance(mydata,list))

# import os,time
# import pyautogui as pag
# try:
#     while True:
#             print("Press Ctrl-C to end")
#             x,y = pag.position() #返回鼠标的坐标
#             posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
#             print (posStr)#打印坐标
#             time.sleep(0.2)
#             os.system('cls')#清楚屏幕
#             # pag.moveTo(100,100,duration=0.25)
#             # pag.moveTo(200,100,duration=0.25)
#             # pag.moveTo(200,200,duration=0.25)
#             # pag.moveTo(100,200,duration=0.25)
# except  KeyboardInterrupt:
#     print ('end....')