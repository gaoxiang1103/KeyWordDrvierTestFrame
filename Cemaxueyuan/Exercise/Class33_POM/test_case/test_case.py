import unittest
import openpyxl
from selenium import webdriver
from Cemaxueyuan.Exercise.Class33_POM.page_object.login_page import LoginPage

driver = webdriver.Chrome()
driver.send


if __name__ =='__main__':
    excel = openpyxl.load_workbook('E:\MyProgram\PycharmProjects\Cemaxueyuan\Exercise\Class33_POM\data\data.xlsx')
    Sheet = excel['Sheet1']
    for v in Sheet.values:
        print(v)
        if type(v[0]) is int:
            data = {}
            data['name'] = v[1]
            data['password'] = v[2]
            driver = webdriver.Chrome()
            lp = LoginPage(driver)
            lp.login(data['name'],data['password'])


