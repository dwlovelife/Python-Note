"""
用户身份验证
"""
# coding=utf-8
userName = input("请输入用户名:\n")
password = input("请输入密妈：\n")
if userName == "admin" and password == "123456":
    print("身份验证成功")
else:
    print("身份验证失败")
