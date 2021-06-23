from selenium import webdriver
from selenium.webdriver.common.by import By

# 对浏览器进行实例化，Edge浏览器调用Edge()，Chrome浏览器调用Chrome()，火狐浏览器调用Firefox()
driver = webdriver.Edge()

url = "http://www.baidu.com"

driver.get(url)

driver.find_element_by_id("kw").send_keys("selenium3")

driver.find_element_by_id("su").click()

driver.find_element(By.ID)
