class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

# 下面是一个对象实体调用方法的常用方式.对象实体a被隐藏的传递给了第一个参数.
a=A()

# 用classmethods装饰,隐藏的传递给第一个参数的是对象实体的类(class A)而不是self.
a.class_foo(1)

# A.foo(1)将会返回一个TypeError错误
# A.foo(1)

# 也可以用类调用class_foo.实际上,如果把一些方法定义成classmethod,那么实际上是希望用类来调用这个方法,而不是用这个类的实例来调用这个方法.
A.class_foo(1)

# 用staticmethods来装饰,不管传递给第一个参数的是self(对象实体)还是cls(类).它们的表现都一样:
a.static_foo(1)
A.static_foo(1)

