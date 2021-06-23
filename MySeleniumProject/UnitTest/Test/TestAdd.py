import unittest
from Calculater import Count
from TestCase import TestCase


class TestAdd(TestCase):
    def test_add01(self):
        c1 = Count(51, 51)
        r1 = c1.add()
        print("两个整数进行相加，计算结果是：", r1)
        self.assertEqual(r1,102)

print(TestAdd("test_add01"))

print(TestAdd().__init__())