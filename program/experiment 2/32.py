nums = input("请输入一个包含若干自然数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

new_list = sorted(nums_list, reverse=True)

print("降序排列后的新列表：", new_list)
