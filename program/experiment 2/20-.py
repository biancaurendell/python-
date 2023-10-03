import random

# 初始化空列表
odd_numbers = []
even_numbers = []

# 随机生成200个在[0, 100]的整数，并按奇偶放入相应列表
for _ in range(200):
    number = random.randint(0, 100)
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# 计算奇数和偶数的个数
num_odd = len(odd_numbers)
num_even = len(even_numbers)

# 输出结果
print("奇数个数：", num_odd)
print("偶数个数：", num_even)
