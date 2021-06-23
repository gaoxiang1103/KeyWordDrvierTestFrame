from Calculater import Count
from TestCase import TestCase

class TestSub(TestCase):
    def test_sub01(self):
        c1 = Count(51,51)
        r1 = c1.sub()
        print("两个整数进行相减，计算结果是：",r1)
        self.assertEqual(r1,0)