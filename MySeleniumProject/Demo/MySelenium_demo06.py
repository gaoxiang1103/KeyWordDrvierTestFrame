from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Firefox()
url = "file:///C:/Users/gaoxiang/Desktop/selenium_demo/demo06.html"
driver.get(url)

# 定位下拉列表元素
mycity = driver.find_element(By.XPATH,"//select[@id='city']")
mynation = driver.find_element(By.XPATH,"//select[@id='nation']")

# 将下拉列表封装为Select对象
mycity1 =Select(mycity)
mynation1= Select(mynation)

# 判断下拉列表是否可以多选
if mycity1.is_multiple:
    print("城市不能多选的！")
else:
    print("城市只能单选！")

#通过选项的索引值进行定位，索引值是从0开始
mycity1.select_by_index(1)

sleep(3)
#通过选项的value属性值进行定位
mycity1.select_by_value("重庆")

# sleep(3)
#通过备选项的文本值进行定位
mycity1.select_by_visible_text("北京")

# 打印所有可选项
print("所有的城市选项都有：")
for item1 in mycity1.options:
    print(item1.text,end="、")

print()

# 打印所有被选中的选项
print("被选中的城市选项有：")
for item2 in mycity1.all_selected_options:
    print(item2.text,end="、")

if mynation1.is_multiple:
    print("民族可以多选！")
else:
    print("民族不可以多选！")

mynation1.select_by_index(3)
mynation1.select_by_value("满族")
mynation1.select_by_visible_text("汉族")

print("民族的可选项有：")
for item3 in mynation1.options:
    print(item3.text,end="、")
print()
print("被选中的民族有：")
for item4 in mynation1.all_selected_options:
    print(item4.text,end="、")
print()

# 打印第一个可选项
print("其中第一个选项是：",mynation1.first_selected_option.text)













