import unittest
from UnitDemo import UnitTestDemo  # 从模块中导入有测试用例的类
from HTMLTestRunner import HTMLTestRunner
import os

# 1、创建一个测试套件
suit = unittest.TestSuite()

# 2.1 将单个测试用例添加进测试套件中，通过测试用例的名称，可通过添加顺序来调整测试用例的执行顺序
suit.addTest(UnitTestDemo('test_case02'))
suit.addTest(UnitTestDemo('test_case01'))

# 2.2 将测试用例放到列表中，然后将列表添加到测试套件中
cases = [UnitTestDemo('test_case02'), UnitTestDemo('test_case01')]
suit.addTests(cases)

# 2.3 将类UnitTestDemo中的用例添加到测试套件中
suit.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitTestDemo))

# 2.4 通过文件名称或文件名称.类名来将测试用例添加到测试套件中
suit.addTests(unittest.TestLoader().loadTestsFromName('UnitDemo'))

# 2.5 基于路径来获取测试用例，discover的返回值就是一个套件，所以不用在创建套件了
case_dir = './'
discover = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='Unit*.py')

# 3、创建一个默认的运行器，并且将日志等级修改为2，日志等级有0、1、2
runner = unittest.TextTestRunner(verbosity=2)
# 4、通过运行器来执行套件
runner.run(discover)

"""
#上面的运行器是unittest框架自带的运行器，还可通过主流的HTMLTestRunner运行器来生成测试报告
"""

# 首先指定报告生成的位置，然后指定报告的名称、报告的标题、报告的描述
report_dir = './report/'
report_file = report_dir + 'report1.html'
title = 'Demo测试报告'
description = '这是第一次生成测试报告，就是练习用的'

if not os.path.exists(report_dir): # 然后判断文件路径是否存在，不存在就创建路径
    os.mkdir(report_dir)

with open(report_file,'wb') as file: # 最后生成测试报告，生成测试报告相当于在文件中生成写入内容
    runner = HTMLTestRunner(stream = file, title = title, description = description)
    runner.run(discover)


