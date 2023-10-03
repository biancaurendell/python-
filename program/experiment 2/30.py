nums = input("请输入一个包含若干整数的列表（用空格分隔）：")
nums_list = [int(num) for num in nums.split()]

odd_list = [num for num in nums_list if num % 2 != 0]
even_list = [num for num in nums_list if num % 2 == 0]

new_list = odd_list + even_list

print("奇数在前，偶数在后的新列表：", new_list)
