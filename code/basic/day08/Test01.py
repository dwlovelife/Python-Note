"""
面向对象
"""
class Student(object):
    #__init__是一个特殊的方法用于创建对象时进行初始化操作
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s正在学习%s'%(self.name, course_name))
    

    #PE8要求标识符的名字用全小写多个单词用下划线链接
    #
    def wacth_movie(self):
        if self.age < 18:
            print('%s只能看一会电视' %self.name)
        else:
            print('%s可以一直看' %self.name)
    

if __name__ == '__main__':
    stu1 = Student('小明', 16)
    stu1.wacth_movie()
    stu1.study('英语')

