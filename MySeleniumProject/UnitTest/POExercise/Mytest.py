from selenium import webdriver
from BusinessLogic import BusinessLogic
import csv

if __name__ =="__main__":
    driver = webdriver.Firefox()
    url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/Demo/demo13.html"
    test = BusinessLogic(driver)
    test.openurl(url)
    file = open("E:/MyProgram/PycharmProjects/MySeleniumProject/UnitTest/POExercise/test.csv",'r')
    data = csv.reader(file)

    print(data)

    for mydata in data:
        print(mydata)
        test.find_username(mydata[0])
        test.find_password(mydata[1])
        test.find_submit()

    test.closebrower()