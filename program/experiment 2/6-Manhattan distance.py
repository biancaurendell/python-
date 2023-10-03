import math

# 输入点的坐标列表
x = input("请输入第一个点的坐标（x1, x2）：").split(',')
y = input("请输入第二个点的坐标（y1, y2）：").split(',')

# 将输入的字符串转换为浮点数
x = [float(coord) for coord in x]
y = [float(coord) for coord in y]

# 计算欧式距离
euclidean_distance = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

# 计算曼哈顿距离
manhattan_distance = abs(x[0] - y[0]) + abs(x[1] - y[1])

print("欧式距离：", euclidean_distance)
print("曼哈顿距离：", manhattan_distance)
