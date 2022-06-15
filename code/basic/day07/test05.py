"""
集合排序
"""
def main():
    list = [1, 5, 4, 3, 2, 8]
    list2 = sorted(list, reverse=True)
    print(list2)
    list.sort()
    print(list)

if __name__ == "__main__":
    main()