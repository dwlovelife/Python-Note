"""
求最大公约数
"""
def gcd(x, y):
    (x, y) = (y, x)  if x > y else (x, y)
    for ele in range(x, 0, -1):
        if x % ele == 0 and y % ele == 0:
            return ele

print(gcd(10, 5))

