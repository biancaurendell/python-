nums = input("请输入一个包含若干自然数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

new_list = [len(str(num)) for num in nums_list]

print("每个自然数的位数：", new_list)
