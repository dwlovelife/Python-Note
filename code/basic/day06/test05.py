#coding=utf-8
def foo():
    global a
    a = 200
    print(a)

if __name__ == "__main__":
    a = 100
    foo()
    print(a)