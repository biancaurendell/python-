import random

# 随机生成两个长度为10的列表
list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

# 使用zip函数将两个列表压缩
zipped_list = list(zip(list1, list2))

# 输出结果
print("List 1:", list1)
print("List 2:", list2)
print("Zipped List:", zipped_list)
