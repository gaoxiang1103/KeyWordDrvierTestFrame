from TestAdd import TestAdd
from TestSub import TestSub
from TestMul import TestMul
from TestDiv import TestDiv
import unittest

if __name__ == '__main__':
    '''
    suit = unittest.TestSuite()

    case_add01 = TestAdd("test_add01")
    case_sub01 = TestSub("test_sub01")
    case_mul01 = TestMul("test_mul01")
    case_div01 = TestDiv("test_div01")

    suit.addTest(case_add01)
    suit.addTest(case_sub01)
    suit.addTest(case_mul01)
    suit.addTest(case_div01)

    runner = unittest.TextTestRunner()
    runner.run(suit)
    '''

test_dir = "../"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="Test*.py")
runner = unittest.TextTestRunner()
runner.run(discover)