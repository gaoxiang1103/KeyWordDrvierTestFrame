'''
@auther:高翔
@email:gaoxiang1103@163.com
@time:2021/5/25
'''
dict01 = {'sex': '男', 'height': '163'}
# 增加键值对
dict01['weight'] = '110'
print(dict01)

#修改键值对
dict01['sex']='女'
print(dict01)

#删除键值对

dict01.pop('sex')
print(dict01)

dict01.popitem()
print(dict01)

del dict01['height']
print(dict01)

#合并两个字典,键值存在，则更新值，减值不存在，则添加值
dict02 = {'sex': '男', 'height': '163'}
dict03 = {'sex': '女', 'weight': '110'}

dict02.update(dict03)
print(dict02)

#字典转为字符串
dict04 = {'sex': '男', 'height': '163'}
str01 = str(dict04)
print(str01,type(str01))

#将字符串转为字典
str02 = eval(str01)
print(str02,type(str02))

for i ,j in dict04.items():
    print(i,j)


