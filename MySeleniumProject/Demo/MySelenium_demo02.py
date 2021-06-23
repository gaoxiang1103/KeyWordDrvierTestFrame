from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# import selenium

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo03.html"
driver.get(url)
# 对单选框元素进行定位
male = driver.find_element(By.ID, "male")
female = driver.find_element(By.ID, "female")
# 对多选框元素进行定位
wangyin = driver.find_element(By.ID, "wangyin")
weixin = driver.find_element(By.ID, "weixin")
zhifubao = driver.find_element(By.ID, "zhifubao")
baiduqianbao = driver.find_element(By.ID, "baiduqianbao")

music = driver.find_element(By.ID, "music")
mounting = driver.find_element(By.ID, "mounting")
travel = driver.find_element(By.ID, "travel")
reading = driver.find_element(By.ID, "reading")

# 对提示信息进行定位
tishi1 = driver.find_element(By.ID, "xingbie")
tishi2 = driver.find_element(By.ID, "zhifu")
tishi3 = driver.find_element(By.ID, "aihao")

female.click()
# 判断性别的选择项
if male.is_selected():
    print("性别选择的是：", male.get_attribute("value"))
else:
    print("性别选择的是：", female.get_attribute("value"))

weixin.click()
# sleep(0.5)
wangyin.click()
# sleep(0.5)
zhifubao.click()
'''
if zhifubao.is_selected():
    print("支付方式选取了%s"%(zhifubao.get_attribute("value")))
elif weixin.is_selected():
    print("支付方式选取了%s"%(weixin.get_attribute("value")))
elif wangyin.is_selected():
    print("支付方式选取了%s"%(wangyin.get_attribute("value")))
elif baiduqianbao.is_selected():
    print("支付方式选取了%s"%(baiduqianbao.get_attribute("value")))
else:
    print("没有选择支付方式")
'''
zhifu = driver.find_elements(By.NAME,"pay")
zhifufangshi =[]
for i in zhifu:
    if i.is_selected():
        zhifufangshi.append(i.get_attribute("value"))
    elif len(zhifufangshi) == 0 :
        print("没有选中的支付方式")
print("选中的支付方式有：",zhifufangshi)

music.click()
# sleep(0.5)
mounting.click()
# sleep(0.5)
reading.click()

xingqu1 = [music.is_selected(), mounting.is_selected(), travel.is_selected(), reading.is_selected()]
xingqu2 = [music.get_attribute("value"), mounting.get_attribute("value"), travel.get_attribute("value"), reading.get_attribute("value")]

str1 = "兴趣爱好选择的是："
for item1, item2 in zip(xingqu1, xingqu2):
    if item1 == True:
        str1 = str1 + item2 + "、"
print(str1)
#获取静态文本的值
# print(tishi1.text)
# print(tishi2.text)
# print(tishi3.text)


