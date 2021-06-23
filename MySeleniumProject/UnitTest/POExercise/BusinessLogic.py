import selenium
from selenium import webdriver
import PublicInformation
import ElementsPath


from PublicInformation import PublicInformation
from ElementsPath import ElementsPath

class BusinessLogic(PublicInformation):
    def __init__(self, driver):
        PublicInformation.__init__(self, driver)
        self.EP = ElementsPath()

    def find_username(self, username):
        self.username = self.driver.find_element(*self.EP.username)
        self.username.send_keys(username)

    def find_password(self, password):
        self.password = self.driver.find_element(*self.EP.password)
        self.password.send_keys(password)

    def find_submit(self):
        self.submit = self.driver.find_element(*self.EP.submit)
        self.submit.click()
