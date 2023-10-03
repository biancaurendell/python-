import random

# 随机生成10个整数
numbers = [random.randint(0, 100) for _ in range(10)]

# 按字符的字典顺序排序
sorted_by_lexicographic = sorted(numbers, key=lambda x: str(x))

# 按长度排序
sorted_by_length = sorted(numbers, key=lambda x: len(str(x)))

# 转换为整数后比较大小排序
sorted_by_integer = sorted(numbers)

# 输出排序结果
print("随机生成的10个整数：", numbers)
print("按字符的字典顺序排序：", sorted_by_lexicographic)
print("按长度排序：", sorted_by_length)
print("转换为整数比较大小排序：", sorted_by_integer)
