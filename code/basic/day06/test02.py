"""
可变参数
"""
def add(*args):
    result = 0
    for x in args:
        result += x
    return result
print(add(1,2))
print(add(1,2,3))