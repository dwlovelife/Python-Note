"""
集合切片
"""
def main():
    list = [1, 2, 3, 4]
    list.append(5)
    for x in list:
        print(x, end = " ")
    print()
    list2 = list[2:4]
    print(list2)
    list3 = list[::-1]
    print(list3)
    

if __name__ == "__main__":
    main()
    