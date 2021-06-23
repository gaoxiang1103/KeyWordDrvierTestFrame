# 操作文本框/文本域/按钮
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo02.html"
driver.get(url)
mydata1 = {'username': 'xiaomin', 'password': 123789, 'comments': '我的留言就是好好学习'}
mydata2 = {}
#定位元素
myname = driver.find_element_by_id("username")
mypassword = driver.find_element_by_id("password")
mycomments = driver.find_element_by_id("comments")
mysubmit = driver.find_element_by_id("submit")
#清空元素的值，并且为元素赋值
myname.clear()
myname.send_keys(mydata1['username'])
mypassword.clear()
mypassword.send_keys(mydata1['password'])
mycomments.clear()
mycomments.send_keys(mydata1['comments'])
#获取文本框填写的值
mydata2["姓名"] = myname.get_attribute("value")
mydata2["密码"] = mypassword.get_attribute("value")
mydata2["留言"] = mycomments.get_attribute("value")
if mydata1["username"] == mydata2["姓名"] :
    print("输入的数据没有问题，可以继续操作！")
else:
    print("请检查一下，姓名是否为:{username}, 密码是否为:{password}".format(username = 'xiaoming',password = '123789'))

sleep(3)
#判断按钮是否可用，如果可用就点击，如果不可用，就提示！
mybutton = mysubmit.get_attribute("value")
if mysubmit.is_enabled():
    print("%s按钮可用，请继续！"%(mybutton))
    mysubmit.click()
else:
    print("%s提交按钮不可用！"%(mybutton))

driver.quit()



