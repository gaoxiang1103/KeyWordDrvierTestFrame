"""
使用多条件，对元素进行定位
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo05.html"
driver.get(url)

#定位到demo2链接
# link = driver.find_element(By.XPATH,"//a[@id='link'][@target='blank']")
link1 = driver.find_element(By.XPATH,"//a[@id='link' and @target = 'blank']")
link1.click()

# sleep(10)


"""
通配符的使用
"""

# tong = driver.find_elements(By.XPATH,"//a[@id]/*")

"""
常用函数
"""

#获取最后一个a元素节点
link2 = driver.find_element(By.XPATH,"//a[last()]")
link2.click()
#获取元素节点的文本值为“链接到demo1”的元素节点

link3 = driver.find_element(By.XPATH,"//a[text()='链接到demo1']")
link3.click()




# driver.quit()

