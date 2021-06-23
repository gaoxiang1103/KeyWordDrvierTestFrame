from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url = "http://sahitest.com/demo/index.htm"
driver.get(url)

ConfirmPage = driver.find_element(By.LINK_TEXT,"Confirm Page")
ConfirmPage.click()

#定位提示框，并点击确定
ClickForConfirm = driver.find_element(By.XPATH,"//input[1]")
ClickForConfirm.click()
alter1 = driver.switch_to.alert
print("提示信息是：",alter1.text)
alter1.accept()

ts1 = driver.find_element(By.XPATH,"//input[2]")
print("点击确定后的提示信息是：",ts1.get_attribute("value"))


#定位提示框，并点击确定
ClickForConfirm.click()
alter1.dismiss()

print("点击取消后的提示信息是：",ts1.get_attribute("value"))

