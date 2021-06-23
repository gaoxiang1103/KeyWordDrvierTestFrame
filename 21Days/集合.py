names = {'zhangsan','wangwu','zhaoliu','laoba','choujiu'}
print(names)
names.add('gaoda')
print(names)
names.clear()
print(names)

a = ('李白', '杜甫', '李清照')
b = ('李白', '王安石', '杜牧')
c = ('王安石', '杜牧', '李清照')
d = set(a + b + c)
print(d)
print(type(a))

e = 'input("请输入名称")'
print(e)
eval(e)
