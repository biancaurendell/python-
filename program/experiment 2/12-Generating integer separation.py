import random

# 生成1到1e20之间的随机整数
num = random.randint(1, 10**20)

# 将整数转换为字符串，以便分离每个位数
digits = str(num)

# 以逗号分隔输出各个位数
result = ",".join(digits)

print(result)
