from Calculater import Count
from TestCase import TestCase


class TestDiv(TestCase):
    def test_div01(self):
        c1 = Count(51,51)
        r1 = c1.div()
        print("两个整数进行相除，计算结果是：",r1)
        self.assertEqual(r1,1)