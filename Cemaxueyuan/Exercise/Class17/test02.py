from selenium import webdriver
import logging.config

# 调用配置文件来生成日志
# 首先拿到配置文件
logging.config.fileConfig('log.ini')
# 然后拿到日志器
log=logging.getLogger()

driver = webdriver.Edge()
url = "http://www.baidu.com"

try:
    log.info('打开网址{}'.format(url))
    driver.get(url)
except Exception as e:
    log.error('打开网址异常，异常信息为{}'.format(e))

try:
    log.info('对元素进行定位，并输入搜索信息')
    driver.find_element_by_id("kw1").send_keys("selenium3")
except Exception as e:
    log.error('定位元素异常，异常信息为{}'.format(e))

try:
    log.info('点击搜索框，进行搜索')
    driver.find_element_by_id("su").click()
except Exception as e:
    log.error('点击搜索框异常，异常信息为{}'.format(e))