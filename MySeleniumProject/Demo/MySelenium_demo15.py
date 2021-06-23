#frame处理

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
def frame1_play():
    myusername = driver.find_element(By.XPATH,"//*[@id='username']")
    mypassword = driver.find_element(By.XPATH,"//*[@id='password']")
    mycomments = driver.find_element(By.XPATH,"//*[@id='comments']")
    mysubmit = driver.find_element(By.XPATH,"//*[@id='submit']")

    myusername.send_keys("xiaoming")
    mypassword.send_keys("1234567890")
    mycomments.send_keys("五一不加班，但是得学习！")
    mysubmit.click()
    print("在frame1中操作完成")

def frame2_play():
    pay = driver.find_element(By.XPATH,"//*[@id='wangyin']")
    pay.click()
    print("在frame2中操作完成")


#对上下结构的frame进行操作
if __name__ == "__main__":
    url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo15/main1.html"
    driver.get(url)
    #切换到frame1，使用id定位
    driver.switch_to.frame("f1")
    #调用frame1函数
    frame1_play()
    #切换回主窗口
    driver.switch_to.parent_frame()
    #切换到frame2,使用name定位
    driver.switch_to.frame("frame2")
    #调用frame2函数
    frame2_play()

"""
#对左右结构的frame进行操作
if __name__ == "__main__":
    url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo15/main2.html"
    driver.get(url)
    #切换到frame1，使用索引号定位
    driver.switch_to.frame(0)
    #调用frame1函数
    frame1_play()
    #切换回主窗口
    # driver.switch_to.parent_frame()
    driver.switch_to.default_content()
    #切换到frame2,使用name定位
    driver.switch_to.frame(1)
    #调用frame2函数
    frame2_play()
"""

"""
#对iframe进行操作
if __name__ == "__main__":
    url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo15/main3.html"
    driver.get(url)
    #切换到frame1，使用Xpath定位后切换
    frame1 = driver.find_element(By.XPATH,"//iframe[1]")
    driver.switch_to.frame(frame1)
    frame1_play()

    #切换回主窗口
    driver.switch_to.default_content()
    #切换到frame2，使用Xpath定位后切换
    frame2 = driver.find_element(By.XPATH,"//iframe[2]")
    driver.switch_to.frame(frame2)
    frame2_play()
"""


driver.quit()
