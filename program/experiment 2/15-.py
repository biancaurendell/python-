# 输入3个英文单词，以空格分隔
words = input("请输入3个英文单词，以空格分隔：").split()

# 找到长度最大的单词
max_length_word = max(words, key=len)

# 输出结果
print("长度最大的单词是：", max_length_word)
print("长度为：", len(max_length_word))
