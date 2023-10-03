nums = input("请输入一个包含若干整数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

max_value = max(nums_list)

print("列表中的最大值：", max_value)
