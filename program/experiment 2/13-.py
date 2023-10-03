import random
import statistics

# 随机生成20个小于100的整数，并保存在列表中
nums = [random.randint(0, 99) for _ in range(20)]

# 计算平均值、最大值、最小值
mean_val = statistics.mean(nums)
max_val = max(nums)
min_val = min(nums)

# 输出结果
print("随机生成的20个小于100的整数为：", nums)
print("平均值为：", mean_val)
print("最大值为：", max_val)
print("最小值为：", min_val)
