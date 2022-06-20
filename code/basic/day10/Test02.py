"""
异常捕捉
"""
def main():
    f = None
    try:
        f = open('a.txt', 'r', encoding= 'utf-8')
    except FileNotFoundError:
        print('文件未找到异常')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()

