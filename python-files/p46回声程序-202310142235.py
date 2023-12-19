a = input("这是一个回声程序，如果不想玩了请输入‘我不玩了’：")
while a != "我不玩了":
    print(a)
    a = input()
b = input("好玩吗？\n")
if b == "好玩":
    print("幼稚【狗头】")
if b == "不好玩":
    print("你爱玩不玩")
else:
    print("哦！再见！")