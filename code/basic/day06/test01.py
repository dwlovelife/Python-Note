#coding=utf-8
from random import randint

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a = 0, b = 0, c = 0):
    print("a=%d,b=%d,c=%d"%(a,b,c))
    return a + b + c

print(roll_dice())
print(add(1,3))
print(add(b = 1, a = 2, c = 3))