from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo10.html"
driver.get(url)

telphone = driver.find_element(By.XPATH,"//input[1]")
telphone.send_keys("18767890989")

submmit = driver.find_element(By.XPATH,"//input[3]")
submmit.click()

sleep(2)

prompt = driver.switch_to.alert
print("提示信息是：",prompt.text)
prompt.send_keys("20210501")

#点击确定按钮
sleep(2)
prompt.accept()

mytelephone = telphone.get_attribute("value")
number = driver.find_element(By.XPATH,"//input[2]")
mynumber = number.get_attribute("value")

print("我输入的手机号是：%s，验证码是：%s"%(mytelephone,mynumber))

