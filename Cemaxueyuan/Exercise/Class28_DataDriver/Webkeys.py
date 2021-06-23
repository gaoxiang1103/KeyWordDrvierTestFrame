"""
关键字驱动的逻辑代码
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
# 通过反射获取浏览器的类型
def open_browser(type):
    try:
        driver = getattr(webdriver, type)()
    except Exception as e:
        print("浏览器打开异常，异常信息{}".format(e))
    return driver
class WebKeys():
    def __init__(self, txt):
        self.driver = open_browser(txt)

        self.driver.implicitly_wait(10)
    # 定义一个打开网址的方法
    def visit(self, txt):
        self.driver.get(txt)
    # 定义一个定位元素的方法
    def locater_element(self, name, value):
        return self.driver.find_element(name, value)
    # 定义一个输入方法
    def input(self, name, value, txt):
        self.locater_element(name, value).send_keys(txt)
    # 定义一个点击的方法
    def click(self, name, value):
        self.locater_element(name, value).click()
    def wait(self,name,value):
        return WebDriverWait(self.driver,10 ,0.5).until(lambda el: self.locater_element(name, value), message='等待失败')

    # 定义一个断言方法
    def assert_text(self,txt):
        try:
            sleep(3)
            assert txt == self.driver.title , '断言失败'
            return True
        except:
            return False

    # 定义一个关闭浏览器的方法
    def quit(self):
        self.driver.quit()