import unittest
from Test.Calculater import Count

#1.编写测试类，并继承unittest模块中的TestCase类
class TestCount(unittest.TestCase):

    #2.重写setup函数，主要用于测试用例执行前的初始化工作，如变量的定义和附初始值
    def setUp(self):
        print("初始化完成！")

    #3.定义一个函数，用于测试被测函数，主要用于被测类的实例化、被测函数的调用，获得被测函数返回值，通过断言方法比较实际结果与预期结果是否相等
    def test_add1(self):
        print("开始测试两个整数相加的结果！")
        c1 = Count(10,20)
        sum1 = c1.add()
        print("计算结果是：",sum1)

        #4.设置断言，将实际结果sum1与预期结果相比较
        self.assertEqual(sum1,30)

    def test_add2(self):
        print("开始测试两个小数相加的结果！")
        c2 = Count(11.11,22.22)
        sum2 = c2.add()
        if abs(sum2-33.33)<=0.001:
            print("计算结果是：",sum2)
        else:
            print("计算结果不正确")

        self.assertEqual(sum2,33.33)

    #5.重写tearDown
    def tearDown(self):
        print("测试工作结束！")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add1"))
    case2 = TestCount("test_add2")
    suite.addTest(case2)
    runner = unittest.TextTestRunner()
    runner.run(suite)