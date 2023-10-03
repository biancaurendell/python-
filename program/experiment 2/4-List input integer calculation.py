nums = input("请输入一些整数，以空格分隔：")
num_list = nums.split()                    # 以空格为分隔符将输入的整数划分为字符串列表
num_list = [int(num) for num in num_list]   # 将字符串转换为整型列表
if len(num_list) > 0:
    average = sum(num_list) / len(num_list) # 计算平均值
    maximum = max(num_list)                 # 获取最大值
    minimum = min(num_list)                 # 获取最小值
    print("平均值为：", average)
    print("最大值为：", maximum)
    print("最小值为：", minimum)
else:
    print("没有输入任何整数。")
