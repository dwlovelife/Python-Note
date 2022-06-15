"""
使用列表
"""
def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = ['hello'] * 5
    list1.append(6)
    list1 += [7]
    print(list1)
    list1.remove(1)
    del list1[0]
    print(list1)
    print(list2)
    if 5 in list1:
        list1.remove(5)
    print(list1)

if __name__ == "__main__":
    main()
