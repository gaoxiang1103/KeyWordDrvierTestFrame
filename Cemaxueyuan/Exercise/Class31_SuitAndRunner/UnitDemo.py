from selenium import webdriver
import unittest
from time import sleep

class UnitTestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 在执行每个用例前，都会先执行setUp与tearDown函数
    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #
    # def tearDown(self) -> None:
    #     sleep(3)
    #     self.driver.quit()

    def test_case01(self):
        # self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element('xpath','//input[@id="kw"]').send_keys('unittest')
        self.driver.find_element('xpath','//input[@id="su"]').click()
        # self.driver.quit()
        sleep(3)
        self.assertEqual('unittest_百度搜索',self.driver.title)

    def test_case02(self):
        # self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element('xpath','//input[@id="kw"]').send_keys('pytest')
        self.driver.find_element('xpath','//input[@id="su"]').click()
        sleep(3)
        self.assertEqual('pytest_百度搜索',self.driver.title)
        # self.driver.quit()

if __name__ == '__mian__':
    unittest.main()




