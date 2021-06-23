from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url = "http://sahitest.com/demo/index.htm"
driver.get(url)

AlterTest = driver.find_element(By.XPATH,"//a[contains(text(),'Alert Test')]")
AlterTest.click()

#获取当前页的url
print("当前页的Title:",driver.title)
print("当前页的Url:",driver.current_url)

AlterMessage = driver.find_element(By.XPATH,"//input[1]")
AlterMessage.clear()
AlterMessage.send_keys("请正确输入提示信息！")

#定位提示框，并点击确定
ClickForAlert = driver.find_element(By.XPATH,"//input[2]")
ClickForAlert.click()
alter1 = driver.switch_to.alert
print("第一个提示信息是：",alter1.text)
alter1.accept()

#定位提示框，并点击确定
ClickForMultilineAlert = driver.find_element(By.XPATH,"//input[3]")
ClickForMultilineAlert.click()
alert2 = driver.switch_to.alert
print("第二个提示信息是：",alert2.text)
alert2.accept()

