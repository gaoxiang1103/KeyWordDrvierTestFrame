class Person(object):
    __slots__ = ("name","age")

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print(self.name + "快跑")

p1 = Person("小明", 18)
print('0x%x' % id(p1))
p1.run()

#weight属性在solts中未定义，因此不能添加
# p1.weight= '105'
# print(p1.weight)


