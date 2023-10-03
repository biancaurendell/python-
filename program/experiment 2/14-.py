import random

# 随机生成4x5的列表
matrix = [[random.randint(0, 100) for _ in range(4)] for _ in range(5)]

# 找到最大的列表
max_list = max(matrix, key=lambda x: max(x))

# 找到和值最大的列表
sum_max_list = max(matrix, key=lambda x: sum(x))

# 输出结果
print("随机生成的4x5的列表为：")
for row in matrix:
    print(row)

print("最大的列表为：", max_list)
print("和值最大的列表为：", sum_max_list)
