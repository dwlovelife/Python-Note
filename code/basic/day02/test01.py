#coding=utf-8
"""
请输入年份判断该年份是平年还是闰年
"""
year = int(input("请输入年份数据："))
is_leap_year  =  year % 4 == 0 and year % 100 != 0 and year % 400 == 0
print("是不是闰年:%s" %is_leap_year)
