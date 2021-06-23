import time

def cal_time(fn):
    print('我是外部函数，我被调用了')
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时',end - start)

    return inner

@cal_time #第一：调用cal_time函数，第二：将demo函数传给fn
def demo():
    x = 0
    for i in range(1,1000000):
        x+=i
    print(x)

demo() #第三：调用demo函数时，已经不是原始的demo函数了，而是已经被装饰过后的demo函数
