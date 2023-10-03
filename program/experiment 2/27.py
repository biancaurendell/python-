data = input("请输入一个包含若干任意数据的列表（用逗号分隔）：")
data_list = eval(data)  # 将输入的字符串转换为实际列表

true_list = [value for value in data_list if value]

print("等价于True的元素组成的列表：", true_list)
