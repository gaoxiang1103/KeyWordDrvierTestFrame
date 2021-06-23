#显示等待

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo12.html"
driver.get(url)

#实例化WebDriverWait类
try:
    w1 = WebDriverWait(driver, 10, 0.5)
    # 调用expected_conditions里的方法判断元素是否存在
    username_locator = (By.XPATH, "//input[11]")
    username = expected_conditions.presence_of_element_located(username_locator)
    # 调用WebDriverWait的until函数等待元素
    username = w1.until(username)
    username.send_keys("小明")
except TimeoutException as e:
    print("超时未定位到相关元素，抛出异常：",e)
finally:
    sleep(3)
    driver.quit()





