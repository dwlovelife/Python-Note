from random import randint
from time import time, sleep


def download_task(filename):
    print("开始下载:" ,filename)
    # 模拟下载任务
    timeToDownload = sleep(5)
    print("%s下载完成!" % filename)


def main():
    start = time()
    download_task("python从入门到精通.pdf")
    download_task("bilibili.avi")
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
