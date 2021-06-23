from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class BasePage:
    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def visit(self, txt):
        self.driver.get(txt)

    def locator(self, method, value):
        return self.driver.find_element(method, value)

    def input(self, method, value, keys):
        self.locator(method, value).send_keys(keys)

    def click(self, method, value):
        self.locator(method,value).click()

    def quit(self):
        self.driver.quit()

    def wait(self , method ,value):
        return WebDriverWait(self.driver, 10 ,0.5).until(lambda el :self.locator(method , value),message = '等待失败')

    def assert_txt(self,method , value,txt):
        try:
            assert txt == self.locator(method , value).text,'断言失败'
            return True
        except:
            return False
