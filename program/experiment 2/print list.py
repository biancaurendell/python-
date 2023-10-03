# 输入一个整数
num = int(input("请输入一个整数："))

# 将整数的每一位拆分为列表元素
digits = [int(digit) for digit in str(num)]

# 计算列表中所有元素的和
total = sum(digits)

# 输出列表和总和
print("每一位列表：", digits)
print("列表元素的和：", total)