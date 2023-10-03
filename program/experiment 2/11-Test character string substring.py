def check_substring(string, lst):
    for substring in lst:
        if substring in string:
            return True
    return False

# 输入字符串和列表
string = input("请输入一个字符串：")
lst = input("请输入一个以逗号分隔的列表，元素之间不要有空格：").split(',')

# 调用函数判断字符串是否包含列表中某个元素作为子串
result = check_substring(string, lst)

print(result)
