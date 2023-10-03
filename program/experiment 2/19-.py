import random
import math

# 使用range函数生成1到10的数字，并计算乘积
product_range = math.prod(range(1, 11))

# 使用random模块生成三个小于10的随机整数，并计算乘积
random_numbers = [random.randint(1, 9) for _ in range(3)]
product_random = math.prod(random_numbers)

# 输出结果
print("1到10的数字的乘积：", product_range)
print("随机生成的三个小于10的数字：", random_numbers)
print("随机数字的乘积：", product_random)
