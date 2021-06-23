from Test.Calculater import Count


class TestCount():
    def test_add(self):
        c1 = Count(10, 20)
        sum1 = c1.add()
        if sum1 == 30:
            print("输出结果是正确的的！")
        else:
            print("加法计算错误！")
        print("计算结束，结果为：", sum1)


MyTestCount = TestCount()
MyTestCount.test_add()
