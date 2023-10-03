nums = input("请输入一些整数，以逗号分隔：")
num_list = nums.split(',')                 # 以逗号为分隔符将输入的整数划分为列表
num_sum = 0
for num in num_list:
    num_sum += int(num)                    # 将输入的每个整数转换为整型并求和
if len(num_list) > 0:
    avg = num_sum / len(num_list)           # 计算平均值
    print("平均值为：", avg)
else:
    print("没有输入任何整数。")