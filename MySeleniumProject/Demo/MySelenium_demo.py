from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
url = "file:///E:/MyProgram/PycharmProjects/MySeleniumProject/id.html"
username="张三"
password="1234567890"
driver.get(url)

myname=driver.find_element(By.ID,"username")
# myname=driver.find_element_by_id("username")
myname.send_keys(username)

time.sleep(2)

mypassword=driver.find_element_by_id("password")
mypassword.send_keys(password)

time.sleep(2)

driver.find_element_by_id("tijiao").click()

# driver.close()
driver.quit()