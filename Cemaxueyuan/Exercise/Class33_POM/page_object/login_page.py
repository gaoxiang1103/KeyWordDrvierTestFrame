from selenium import webdriver
from Cemaxueyuan.Exercise.Class33_POM.base_page.base_page import BasePage

class LoginPage(BasePage):
    defaults_url = 'http://39.98.138.157/shopxo/index.php'
    url = defaults_url + '?s=/index/user/logininfo.html'

    # username = ('xpath','//input[@name = "accounts"]')
    # password = ('name','pwd')
    # login_button = ('xpath','//button[text()="登录"]')

    def login(self,user ,pwd):
        self.visit(self.url)
        self.input('xpath','//input[@name = "accounts"]',user)
        self.input('name','pwd',pwd)
        self.click('xpath','//button[text()="登录"]')

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     user = 'yunfei'
#     pwd = '1234567890'
#     lp = LoginPage(driver)
#     lp.login(user,pwd)





