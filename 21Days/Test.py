names = ["张三", "李四", "赵六", "王五", "龙七", "龙七"]
# print(names[3])
# names[3] = '赵七'
# print(names[3])
# print(names)
# temp = input("请输入小伙伴的名称：")
# names.append(temp)
# print(names)
# names.insert(3, "主使")
# print(names)
# xingming = ['wangba', 'gaoyi', 'longsan']
# names.extend(xingming)
# print(names)
#
# findname = input("请输入要查找的姓名：")
# if findname in names:
#     print("找到了")
# else:
#     print("没找到")

# print(names.index('龙七', 5, 6))
# print(names.count("龙七"))
# del names[2]
# print('---删除之后的列表元素---%s' % names)
# # names.pop()
# # print('---删除之后的列表元素---%s' % names)
# names.remove("龙七")
# print('---删除之吼吼的列表元素---%s' % names)
# names.clear()
# print('---清空之后的列表元素---%s' % names)
# length = len(names)
# i = 0
# while i <length:
#     print(names[i])
#     i += 1
# for name in names:
#     print(name)
# a = 5
# b = 6
# a,b = b,a
# print(a)
# print(b)
x = [1,2,3,4,5]
y = x
z= x.copy()
x[0] = 3
print(y)
print(z)

import copy
a = copy.copy(x)
x2 = x[::]
print(x2)