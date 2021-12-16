def factorial(num):
    """
    求阶乘
    """
    result = 1
    for x in range(1, num + 1):
        result *= x
    return result

m = int(input("请输入m:"))
n = int(input("请输入n:"))
print(factorial(m)//factorial(n)//(factorial(m - n)))