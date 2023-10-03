def check_any_true(lst):
    return any(lst)

# 输入列表
lst = input("请输入一个列表，元素以逗号分隔：").split(',')

# 将输入的字符串转换为布尔值
lst = [bool(element) for element in lst]

# 调用函数判断列表中是否存在至少一个真值
result = check_any_true(lst)

print(result)
