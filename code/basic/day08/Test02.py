"""
访问可见性
"""
class Test:
    def __init__(self, foo):
        self.__foo = foo;
    
    def __bar(self):
        print(self.__foo)
        print('__bar')

if __name__ == "__main__":
    test = Test("foo")
    test._Test__bar()
