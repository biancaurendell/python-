from functools import reduce
import operator

nums = input("请输入一个包含若干整数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

product = reduce(operator.mul, nums_list)

print("这些整数的乘积：", product)
