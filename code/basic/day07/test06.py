"""
用列表的生成试语法来创建列表
"""
import sys

def main():
    list = [x for x in range(1,10)]
    print(list)
    list2 = [x + y for x in "ABCDE" for y in "12345"]
    print(list2)
    f = [x ** 2 for x in range(1,10)]
    print(sys.getsizeof(f))

if __name__ == "__main__":
    main()