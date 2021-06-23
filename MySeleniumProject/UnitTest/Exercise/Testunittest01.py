from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class testunittest_01(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Firefox()
      self.driver.implicitly_wait(10)
      self.url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/Unittest/unittest.html"
      print("初始化完成")

    def test_unittest(self):
      driver = self.driver
      driver.get(self.url)
      driver.find_element(By.ID,"username").clear()
      driver.find_element(By.ID,"username").send_keys("xiaoming")
      driver.find_element(By.ID,"password").clear()
      driver.find_element(By.ID,"password").send_keys("1234567890")
      driver.find_element(By.ID,"comments").clear()
      driver.find_element(By.ID,"comments").send_keys("五一就好好学习吧")
      driver.find_element(By.ID,"submit").click()

    def tearDown(self):
      self.driver.quit()

if __name__ =="__main__":
  unittest.main()





