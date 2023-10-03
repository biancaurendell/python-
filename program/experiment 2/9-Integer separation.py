# 输入整数
num = int(input("请输入一个整数："))

# 将整数转换为字符串，以便分离每个位数
digits = str(num)

# 计算各个位数之和
total = sum(int(digit) for digit in digits)

print(total)
