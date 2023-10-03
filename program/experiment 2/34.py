nums = input("请输入一个包含若干数字的列表（用空格分隔）：")
nums_list = [float(num) for num in nums.split()]

abs_max = max(nums_list, key=abs)

print("绝对值最大的数字：", abs_max)
