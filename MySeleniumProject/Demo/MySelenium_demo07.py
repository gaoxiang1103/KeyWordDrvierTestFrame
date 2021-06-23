from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo07.html"
driver.get(url)

pay = driver.find_elements(By.NAME,"pay")
for i in pay:
    if i.is_selected():
        print(i.get_attribute("value"))
    else:
        i.click()
        print("点击：",i.get_attribute("value"))

print("-----------------------------------------------------------")

aihao = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
a1=[]
a2=[]
a3=[]
for a in aihao:
    if a.get_attribute("name") == "爬山":
        a.click()

    m = a.is_selected()
    a1.append(m)
    n = a.get_attribute("name")
    a2.append(n)
print(a1)
print(a2)

s1 = "选则的爱好有："
for a11, a22 in zip(a1,a2):
    if(a11 == True):
        s1 = s1 + a22 + "、"
print(s1)








