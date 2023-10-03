
# 输入一个整数
num = int(input("请输入一个整数："))

# 输出二进制、八进制、十六进制表示
binary = bin(num)
octal = oct(num)
hexadecimal = hex(num)

print("二进制表示：", binary)
print("八进制表示：", octal)
print("十六进制表示：", hexadecimal)

# 输出整数的最大值和最小值
max_value = max(num, 0)
min_value = min(num, 0)

print("整数的最大值：", max_value)
print("整数的最小值：", min_value)