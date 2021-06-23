'''
    测试套件：
        就相当于是一个list，说白了就是一个文件夹
        在默认的UnitTest框架下，所有的用例都是会全部执行，且执行时是依照UnitTest自定义的排序规则来实现的。
        如果想要改变默认的UnitTest运行顺序，可以通过套件添加用例来实现。
        如果说需要调用部分的测试用例，来执行冒烟测试，就无法在默认的UnitTest下实现。
        所以可以基于套件的形态将需要调用的测试用例提取出来进行执行，从而自动化实现测试效果
        还可以基于jenkins持续集成时，一键运行指定测试用例
        甚至于在用例并发运行时，也可以通过调用套件来实现并行处理。
    运行器：
        是UnitTest下的测试结果生成
        主流的UnitTest下的运行器测试报告HTMLTestRunner。
        环境部署：
            不能够通过pip install安装
            下载HTMLTestRunner.py文件，放到python安装路径下的Lib文件夹中。
            修改py文件的源码：
                第94行，将import StringIO修改成import io
                第539行，将self.outputBuffer = StringIO.StringIO()修改成 self.outputBuffer = io.StringIO()
                第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
                第766行，将uo = o.decode('latin-1')修改成uo = e
                第772行，将ue = e.decode('latin-1')修改成ue = e
                第631行，将print >> sys.stderr, '\nTime Elapsed: %s' %  (self.stopTime-self.startTime)修改成print(sys.stderr, '\nTime  Elapsed: %s' % (self.stopTime-self.startTime))
            如果这样你都不会改了，就下载我发到群里的文件就可以了。

'''
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
# from HTMLTestReportCN import HTMLTestRunner

from UnitDemo import UnitTestDemo
# 创建套件
suite = unittest.TestSuite()
# 1. 添加用例到套件：添加单个测试用例，通过测试用例的名称来添加。
suite.addTest(UnitTestDemo('test_04'))
suite.addTest(UnitTestDemo('test_03'))
suite.addTest(UnitTestDemo('test_01'))
# 2. 添加多个用例到套件：可以基于list来实现
# cases = [UnitDemo('test_02'), UnitDemo('test_01'), UnitDemo('test_03')]
# suite.addTests(cases)
# 3. 添加多个用例到套件：通过添加一整个UnitTest类作为套件中的用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))
# 4. 添加多个用例到套件，通过Name来实现，这里不能直接写class名称，只能写文件名称或者文件名.class名
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_demo.UnitDemo'))
# 5. 批量添加：通过文件名批量添加
# 定义用例的路径
case_dir = './'
# 基于路径来获取用例，组成套件:discover方法返回值就是一个suite，所以不需要创建套件了。
discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='u*.py')
# 套件的运行：一定要结合运行器来实现
# 1. 创建默认的运行器:verbosity是日志等级，0-1-2
# runner = unittest.TextTestRunner(verbosity=2)
# # 2. 基于运行器来执行套件
# runner.run(discover)
# 基于HTMLTestRunner生成测试报告
# 基本的报告配置
# 报告的保存路径
report_dir = './report/'
# 报告名称
report_file = report_dir + 'report3.html'
# title
title = 'DEMO系统的测试报告'
# description
description = '本次是属于0.1版本的首轮冒烟测试执行结果'
#  判断报告路径是否存在。
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
# 生成HTMLTestRunner测试报告相当于在文件中写入内容
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title=title,
                            description=description)
    runner.run(discover)
