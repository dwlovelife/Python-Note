#coding=utf-8
"""
判断年份是否为闰年
"""
year=int(input("请输入年份:\n"))
is_leap=(year % 4 == 0 and year % 100 != 0 and year % 400 == 0)
print(is_leap)

