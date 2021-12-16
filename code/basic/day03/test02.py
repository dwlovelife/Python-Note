"""
投色子决定做什么事情
"""
#coding=utf-8
from random import randint
num = randint(1,6)
print("当前色子数:%d"%num)
if num == 1:
    print("吃饭")
elif num == 2:
    print("睡觉")
elif num == 3:
    print("遛狗")
else:
    print("看电视")