"""
包装器练习
"""


class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter方法

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 18:
            print('不能玩手机游戏')
        else:
            print('可以玩手机游戏')


def main():
    person = Person('Jack', 11)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
