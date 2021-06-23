import urllib
import urllib.request
import re
import random
# #将数据保存在内存中
# try:
#     data = urllib.request.urlopen("http://www.jd.com").read().decode("utf-8","ignore")
#     print(len(data))
# except Exception as err:
#     print ("可能地址没有找到，请确认是否联网或地址是否可访问！")
#
# pat = "<title>(.*?)</title>"
# # re.S的作用是当data中的数据有换行的时候，会将其当做一个整体进行匹配，否则会在每一行中查找。
# result = re.compile(pat,re.S).findall(data)
# print(result)

# urllib.request.urlretrieve("http://www.jd.com",filename = "E:\\MyProgram\\PycharmProjects\\21Days\\jd.html")


