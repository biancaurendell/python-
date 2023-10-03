import random

# 使用dir函数查看random库中的函数和属性
print(dir(random))

# 使用help函数获取特定函数的帮助信息
help(random.random)
help(random.randint)

# 使用random库生成随机数
random_number = random.random()   # 生成0到1之间的随机浮点数
random_integer = random.randint(1, 10)   # 生成1到10之间的随机整数

print("Random number:", random_number)
print("Random integer:", random_integer)