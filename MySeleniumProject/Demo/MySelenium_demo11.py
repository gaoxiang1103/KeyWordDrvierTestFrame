#多窗口操作

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/Demo/demo11.html"
driver.get(url)

#获得当前窗口的句柄
h1 = driver.current_window_handle
print("当前窗口的句柄是：",h1)

l2 = driver.find_element(By.LINK_TEXT,"链接到demo2")
l2.click()

#获得所有打开窗口的句柄
AllHandle1 = driver.window_handles
print("当前所有打开的窗口的句柄是：",AllHandle1)

#先打开第一个窗口，然后退回
l1 = driver.find_element(By.LINK_TEXT,"链接到demo1")
l1.click()
driver.back()

#对第二个超链接进行操作
for i in AllHandle1:
    if i != h1:
        driver.switch_to.window(i)
        print("当前页面的标题是：",driver.title)
        print("当前页面的地址是：",driver.current_url)
        h2 = driver.current_window_handle
        print("当前窗口的句柄是：",h2)
        myusername = driver.find_element(By.XPATH,"//*[@id='username']")
        mypassword = driver.find_element(By.XPATH,"//*[@id='password']")
        mycomments = driver.find_element(By.XPATH,"//*[@id='comments']")
        mysubmit = driver.find_element(By.XPATH,"//*[@id='submit']")
        myusername.send_keys("hello")
        mypassword.send_keys("1234567890")
        mycomments.send_keys("五一放假不回家，在宁波学习！")
        mysubmit.click()
for j in AllHandle1:
    if j==h1:
        driver.switch_to.window(j)
        l3 = driver.find_element(By.LINK_TEXT,"链接到demo3")
        l3.click()

AllHandle2 = driver.window_handles
print("当前所有打开的窗口的句柄是：",AllHandle2)

for k in AllHandle2:
    if k !=h1 and k != h2:
        driver.switch_to.window(k)
        pay = driver.find_element(By.XPATH,"//*[@id='wangyin']")
        pay.click()
        sleep(3)
        driver.close()


        







