# 输入整数
num = int(input("请输入一个整数："))

# 将整数转换为字符串，以便分离每个位数
digits = str(num)

# 以逗号分隔输出各个位数
result = ",".join(digits)

print(result)
