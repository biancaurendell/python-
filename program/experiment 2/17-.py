import random

# 随机生成两个长度为10的列表
list1 = [random.randint(1, 10) for _ in range(10)]
list2 = [random.randint(1, 10) for _ in range(10)]

# 对应位置的数相加
add_result = [x + y for x, y in zip(list1, list2)]

# 对应位置的数相乘
multiply_result = [x * y for x, y in zip(list1, list2)]

# 对应位置的数相乘后求和（向量内积）
dot_product = sum(x * y for x, y in zip(list1, list2))

# 输出结果
print("随机生成的两个列表：")
print("List1:", list1)
print("List2:", list2)
print("对应位置的数相加结果：", add_result)
print("对应位置的数相乘结果：", multiply_result)
print("向量内积结果：", dot_product)
