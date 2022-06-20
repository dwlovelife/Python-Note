"""
_slots_魔法
"""

class Person(object):
    #限定person对象只能绑定 name,age,gender对象
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name


    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    def paly(self):
        if self.age < 18:
            print('不能玩手机游戏')
        else: 
            print('可以玩手机游戏')

def main():
    person = Person('jack', 17)
    person.paly()
    person._gender = '男'
    person._g = '男'
    print(person._g)


if __name__ == '__main__':
    main()