from multiprocessing import Process
from os import getpid
from time import sleep,time

def download_task(filename):
    print("当前进程id[%d]"%getpid())
    print("开始下载:",filename)
    sleep(5)
    print("下载完成")

def main():
    start = time()
    p1 = Process(target=download_task,args=('python从入门到精通.pdf',))
    p1.start()
    p2 = Process(target=download_task,args=('颈椎病康复指南.pdf',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("花费时间为:%d"%(end - start))

if __name__ == "__main__":
    main()