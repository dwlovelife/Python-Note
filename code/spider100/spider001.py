import requests
import threading #多线程模块
import re   #正则表达式模块
import time #时间模块
import os   #目录操作模块

 #图片列表页面的数组
all_urls = []
all_iamge_urls = []
lock = threading.Lock()
class Spider():
    # 构造函数初始化数据使用
    def __init__(self, targetUrl):
        self.targetUrl = targetUrl

    # 获取所有的想要抓去的URL
    def getUrls(self, startPage, pageNum):
        for i in range(startPage, pageNum+1):
            url = self.targetUrl % i
            all_urls.append(url)

#生产者，负责从每个页面提取图片列表的链接
class Producer(threading.Thread):

    def run(self,startPoint,endPoint):
        for x in range(startPoint,endPoint)
            page_url = all_urls[x]
            response = requests.get(page_url,timeout=3)
            allPicLink = re.findall('<a class="image-box" href="(.*?)" target="_blank" style="width:100%;height:100%;">',response.text,re.S)
            all_iamge_urls.extend(allPicLink)
            #print("结果为:",all_iamge_urls)


def main():
    targetUrl = "https://www.51miz.com/png/p_%d/"
    spider = Spider(targetUrl)
    spider.getUrls(1,10)

    #定义线程集合 为4个线程
    threads = []
    threadNum = 4
    #同时将任务分成四等份
    taskNum = len(all_urls) // threadNum

    startPoint = 0
    endPoint = 1
    #开启两个线程去访问
    for x in range(1,threadNum+1):
        if x == threadNum:
            endPoint = len(all_urls)

        t = Producer()
        t.start()
        threads.append(t)
    for tj in threads:
        tj.join()


if __name__ == "__main__":
    main()