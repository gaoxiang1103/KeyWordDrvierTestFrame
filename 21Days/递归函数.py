def fuc(num):
    result = 1
    if num == 1:
        return 1
    result = num * fuc(num - 1)
    return result


print(fuc(5))
