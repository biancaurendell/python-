nums = input("请输入一个包含若干整数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

str_list = [str(num) for num in nums_list]

print("转换后的字符串列表：", str_list)
