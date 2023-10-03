temperature = input("请输入温度值：")

if temperature.endswith('C') or temperature.endswith('c'):
    celsius = float(temperature[:-1])
    fahrenheit = celsius * 1.8 + 32
    print("转换后的华氏温度为：{:.2f}F".format(fahrenheit))

elif temperature.endswith('F') or temperature.endswith('f'):
    fahrenheit = float(temperature[:-1])
    celsius = (fahrenheit - 32) / 1.8
    print("转换后的摄氏温度为：{:.2f}C".format(celsius))

else:
    print("输入格式错误，请以C或F结尾，表示摄氏或华氏温度。")