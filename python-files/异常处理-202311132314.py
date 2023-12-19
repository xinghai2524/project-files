
try:
    num = eval(input("请输入数字"))
    print(num ** 2)
except NameError:
    print("注意格式")
except SyntaxError:
    print("请输入数字")
else:
    print("程序运行正常")
finally:
    print("程序结束，不知道有没有错误")
