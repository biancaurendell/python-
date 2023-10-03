nums = input("请输入一个包含若干自然数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

avg = sum(nums_list) / len(nums_list)
avg = round(avg, 3)

print("平均值为：", avg)
