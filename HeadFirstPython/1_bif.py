"""
内置函数
"""

# 区间迭代
for item in range(10):
    print(item)

# open 打开文件
import os
print(os.getcwd())
data=open('HeadFirstPython/data/雨中小巷.txt',encoding='utf-8')
for r in data:
    print(r)
data.close()