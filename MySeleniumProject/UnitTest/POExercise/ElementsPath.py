#对元素进行定位
from selenium.webdriver.common.by import By

class ElementsPath():
    def __init__(self):
        self.username = (By.XPATH, "//*[@id='username']")
        self.password = (By.XPATH, "//*[@id='password']")
        self.submit = (By.XPATH, "//*[@id='tijiao']")