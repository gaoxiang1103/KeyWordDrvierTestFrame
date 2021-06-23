
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo04.html"
driver.get(url)

#标记存在的某个子标记
l1 = driver.find_element(By.XPATH,"//u1[lable]")

l2 = driver.find_element(By.XPATH,"//u1[li='足球']")

str1 = l1.text
print(str1)

list1 = list(str1)
print(list1)

list2 = str1.split("\n")
print(list2)

