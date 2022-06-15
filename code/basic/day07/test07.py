"""
使用元组
"""
def main():
    t = ("jack", 28, "四川成都")
    print(t)
    print(t[0])
    print(t[2])
    print(t[:2])
    #遍历元组的值
    for number in t:
        print(number)
    list1 = list(t)
    list1[1] = 29
    print(list1)
    friut_list = ("水果", "梨子", "香蕉")
    friue_tuple = tuple(friut_list)
    print(friue_tuple)
    

if __name__ == "__main__":
    main()
