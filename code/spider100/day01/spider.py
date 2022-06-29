#-*- coding=utf-8 -*-
"""
bs4 网页解析,获取数据
re 正则表达式
urllib获取网页数据
xlwt excel操作
sqllite3 进行sqlLite数据库操作
"""
import bs4 
import re
import urllib.request
import xlwt
import sqlite3

def main():
    baseUrl = "https://movie.douban.com/top250?start="
    #1. 爬取网页
    dataList = getData(baseUrl)
    savePath = ".\\豆瓣电影250.xls"


def getData(baseUrl):
    #2. 解析数据
    dataList = []
    return dataList


#保存数据
def saveData(savePath):
    pass




if __name__ == "__main__":
    main()
