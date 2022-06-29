"""
文本测试
"""
def main():
    with open("D://dingwei17//Desktop//a.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
    f.close()
 
if __name__ == "__main__":
    main()
