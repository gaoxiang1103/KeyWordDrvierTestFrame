#lambda表达式
sum = lambda a, b: a + b
print('a+b的结果是:%d' % sum(1, 2))

#自定义一个匿名函数

# def calc(a, b):
#     c = add(a, b)
#     return c
#
# def add(x, y):
#     return x + y
#
#
# total = calc(1, 2)
# print('x + y的结果是：%d' % total)

def calc(a,b,fn):
    c = fn(a,b)
    return c

def add(x,y):
    return x+y

def minus(x,y):
    return x-y

total1 = calc(1,2,add)
print(total1)
total2 = calc(3,5,minus)
print(total2)

