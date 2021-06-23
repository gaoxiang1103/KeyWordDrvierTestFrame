# person = {"name": "xiaotangtang",
#           "Chinese": "78",
#           "Math": "99",
#           "height": 170,
#           'x':'y',
#           "weight": 150,
#           }
# #通过key来获取value
# print(person['name'])
#
# x = 'height'
# print(person[x])
# print(person["x"])
# # print(person["y"])
#
# #如果未找到了可以使用默认值
# print(person.get("s",'fdas'))
#
# person.pop('name')
# print(person)
#
# newperson= person.popitem()
# print(newperson)

#字典的遍历
person = {'name':'小糖糖','height':'180cm','sex':'man'}
# for i in person:
#     print(i,'=',person[i])

#获取到所有key，然后通过key来获取value
for i in person.keys():
    print(i,'=',person[i])

print(person.keys())
#遍历value

for m in person.values():
    print(m)

#将字典转为列表，列表中的数据是元祖，然后将元祖当做整体进行遍历
print(person.items())
for n in person.items():
    print(n)
    print(n[0],'=',n[1])


