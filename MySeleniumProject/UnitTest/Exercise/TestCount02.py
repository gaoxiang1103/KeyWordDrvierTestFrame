from Test.Calculater import Count

Mytest = Count(10.99,9.01)
sum2 = Mytest.add()

if abs(sum2-20.00) <= 0.001:
    print("加法计算正确！")
else:
    print("加法计算错误！")
print("加法计算结果：",sum2)
