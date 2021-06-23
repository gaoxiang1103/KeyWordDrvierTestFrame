nums = (1, 5, 6, 7, 7, 7, 7, 7)
nums.index(7)
print(nums.index(7))
print(nums.count(7))
print(nums[1])
# /只有一个元素的元组
num = (1,)
print(type(num))
print(list(nums))
words = ["我的","你的","我们的","他们的","大家的"]
print(tuple(words))
height = ("178","189","190")
# print("*".join(height))

hello = ['h','e','l','l','o']
print("".join(hello))

for i in nums:
    print(i)

