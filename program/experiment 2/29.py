nums = input("请输入一个包含若干整数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

even_list = [num for num in nums_list if num % 2 == 0]

print("只包含偶数的新列表：", even_list)
