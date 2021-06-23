import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        print("开始测试了")

    def tearDown(self):
        print("测试结束了")