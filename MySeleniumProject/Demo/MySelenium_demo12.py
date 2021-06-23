#隐式等待

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo12.html"

#设置最长等待时间
driver.implicitly_wait(10)
driver.get(url)



try:
    myusername = driver.find_element(By.XPATH,"//input[1]")
    mypassword = driver.find_element(By.XPATH,"//input[2]")
    mysubmit = driver.find_element(By.XPATH,"//input[3]")
    myusername.send_keys("xiaoming")
    mypassword.send_keys("1234567890")
    mysubmit.click()
    print("页面操作正常完成")
except NoSuchElementException as e:
    print("已经等待了10s")
    print("元素定位或操作出现异常，异常信息为：",e)
finally:
    print("程序执行完毕，退出")
    driver.quit()



