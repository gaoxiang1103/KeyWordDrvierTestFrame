"""
关键字驱动的业务代码
"""
from  Web_Keys import WebKeys
from selenium.webdriver.common.by import By

from time import sleep

wb = WebKeys('Chrome')

wb.visit("https://www.baidu.com/")
wb.locater_element(By.XPATH,'//input[@id="kw"]')
wb.wait(By.XPATH,'//input[@id="kw"]')
wb.input('xpath','//input[@id="kw"]','关键字驱动')
wb.click('xpath','//input[@id="su"]')
sleep(3)
wb.title()

sleep(3)
wb.quit()


