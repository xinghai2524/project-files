import random

# 定义函数区
i = 0
a = 1
b = 1000
printtable = "0"

number_2 = random.randint(0, 1000)
number = input("游戏开始，请输入数字")
while number not in ["t", "T"]:
    i += 1
    number = int(number)
    # 判断大小
    if number > number_2:
        print("数字大了，", end="")
        b = number
    elif number < number_2:
        print("数字小了，", end="")
        a = number
    else:
        print("预测了{}次，猜对了".format(i))
        break
    # 让随机数帮忙输入
    number = random.randint(a, b)
    print(number)