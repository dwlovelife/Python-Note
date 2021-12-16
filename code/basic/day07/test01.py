"""
使用字符串或者常用数据结构
"""
def main():
    str = " hello world "
    #通过len计算字符串的长度
    print(len(str))
    #去除字符串两边的空格
    print(str.strip())

    str2 = "abc1234"
    print(str2[2])
    print(str2[::-1])
    print(str2[:3:-1])
    #检查字符串是否由数字构成
    print(str2.isdigit())

if __name__ == '__main__':
    main()
        