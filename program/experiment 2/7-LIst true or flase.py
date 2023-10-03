def check_all_true(lst):
    return all(lst)

# 输入列表
lst = input("请输入一个列表，元素以逗号分隔：").split(',')

# 将输入的字符串转换为布尔值
lst = [bool(element) for element in lst]

# 调用函数判断列表中的元素是否全部为真
result = check_all_true(lst)

print(result)
