nums1 = input("请输入第一个包含若干整数的列表（用空格分隔）：")
vec1 = [int(num) for num in nums1.split()]

nums2 = input("请输入第二个包含若干整数的等长列表（用空格分隔）：")
vec2 = [int(num) for num in nums2.split()]

dot_product = 0
for a, b in zip(vec1, vec2):
    dot_product += a * b

print("这两个向量的内积：", dot_product)
