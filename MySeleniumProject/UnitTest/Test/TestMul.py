from Calculater import Count
from TestCase import TestCase


class TestMul(TestCase):
    def test_mul01(self):
        c1 = Count(51,51)
        r1 = c1.mul()
        print("两个整数进行相乘，计算结果是：",r1)
        self.assertEqual(r1,2601)