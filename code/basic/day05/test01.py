"""
求解百钱百鸡问题
1只公鸡5元 母鸡3元 3只小鸡1元 求100元 买公鸡多少只母鸡多少只小鸡多少只
"""
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if (5 * x + 3 * y +  z/3 ) == 100 :
            print("x:%d,y:%d,z:%d"%(x,y,z))
