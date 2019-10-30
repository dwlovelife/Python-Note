from random import randint
from threading import Thread
from time import time,sleep

def dwonload(filename):
    print("开始下载%s..." %filename)
    sleep(5)
    print("%s下载完成!" %(filename))

def main():
    start = time()
    t1 = Thread(target=dwonload, args=('python从入门到精通.pdf',))
    t1.start()
    t2 = Thread(target=dwonload, args=('颈椎病康复指南.pdf',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("总共耗费了%.3f秒"%(end - start))

if __name__ == "__main__":
    main()