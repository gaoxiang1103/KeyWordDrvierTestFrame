from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo08.html"
driver.get(url)

submmit = driver.find_element(By.XPATH,"//input[@type='button']")
submmit.click()

# 定位Alert对象
alert1 = driver.switch_to.alert
print("提示信息是：",alert1.text)

sleep(2)
# 点击确定按钮
alert1.accept()



