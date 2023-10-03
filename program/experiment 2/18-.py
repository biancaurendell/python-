from functools import reduce

# 生成等差数列
sequence = list(range(1, 50, 3))

# 使用reduce函数求和
sum_of_sequence = reduce(lambda x, y: x + y, sequence)

# 输出结果
print("生成的等差数列：", sequence)
print("数列的和：", sum_of_sequence)
