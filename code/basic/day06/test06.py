"""
python变量的作用域共有四种：
局部作用域（L）
作用于闭包函数外的函数中的作用域（E）
全局作用域（G）
内置作用域 [即内置函数所在的模块范围]（B）
变量在作用域中查找的顺序是 L -> E -> G -> B

"""
global e #全局作用域
def foo():
    c = "hello" #闭包函数外的作用域
    x = 0
    def bar():
        c = "hi"
        b = True
        print(a)
        print(b) #局部作用域
        print(c)
        nonlocal x 
        x = a
        print(x)
    bar()
    print(x)
 


if __name__ == "__main__":
    a = 100
    foo()