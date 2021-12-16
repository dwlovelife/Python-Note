"""
猜数字游戏
"""
#coding=utf-8
from random import randint
num = randint(1,100)
print(num)
counter = 0
while True:
    guessNum = int(input("请输入你猜的数:\n"))
    counter +=1
    if guessNum < num:
        print("大一点")
    elif guessNum > num:
        print("小一点")
    else:
        print("猜对了")
        break
if  counter >= 7 :
    print("智商存疑")
else:
    print("很聪明")