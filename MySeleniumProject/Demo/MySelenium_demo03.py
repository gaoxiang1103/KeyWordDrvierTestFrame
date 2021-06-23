from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo02.html"
driver.get(url)

username = "小明"
password = "123"
comments = "好好学习，天天向上"

"""
# 使用绝对路径，进行xpath定位
myusername = driver.find_element_by_xpath("/html/body/form/u1/li/input[@value='请输入姓名']")
mypassword = driver.find_element_by_xpath("/html/body/form/u1/li/input[@id='password']")
mycomments = driver.find_element_by_xpath("/html/body/form/u1/li/textarea[@id='comments']")
mybutton = driver.find_element_by_xpath("/html/body/form/u1/input[@id='submit']")
"""


# 使用相对路径，进行xpath定位
myusername = driver.find_element(By.XPATH,"//input[@value='请输入姓名']")
mypassword = driver.find_element(By.XPATH,"//input[@id='password']")
mycomments = driver.find_element(By.XPATH,"//textarea")
mybutton = driver.find_element(By.XPATH,"//input[@type='submit']")


myusername.clear()
mypassword.clear()
mycomments.clear()
myusername.send_keys("username")
mypassword.send_keys("password")
mycomments.send_keys("comments")
mybutton.click()

driver.quit()
