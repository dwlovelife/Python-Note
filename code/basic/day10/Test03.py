import imp


import time


def main():
    # 一次性读取文件整个内容
    path = "D://dingwei17//Desktop//dev//常用.txt"
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open(path, mode='r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")

    f = open(path, "r", encoding='utf-8')
    print(f.readlines())
    print(type(f.readlines()))

if __name__ == "__main__":
    main()
