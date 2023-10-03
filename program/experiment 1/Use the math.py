import math

# 使用dir函数查看math库中的函数和属性
print(dir(math))

# 使用help函数获取特定函数的帮助信息
help(math.sqrt)
help(math.sin)

# 使用math库中的函数进行数学计算
x = 4.5
y = math.sqrt(x)   # 开平方根
sin_value = math.sin(math.pi / 2)   # 计算正弦值

print("Square root of", x, "is", y)
print("Sin value of pi/2 is", sin_value)