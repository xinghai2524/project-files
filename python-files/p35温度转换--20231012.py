def temperture(tempstr):
    while tempstr != "退出":
        if tempstr[-1] in ['F', 'f']:
            c = (eval(tempstr[0:-1]) - 32)/1.8
            print("转换后的温度是{:.2f}C".format(c))
        elif tempstr[-1] in ['C', 'c']:
            f = (1.8*eval(tempstr[0:-1]))+32
            print("转换后的温度是{:.2f}F".format(f))
        else:
            print("格式输入错误")
        tempstr = input("************************\n请输入带符号的温度值：\n退出请输入‘退出’")


e = input("************************\n 请输入带符号的温度值：\n退出请输入‘退出’")
temperture(e)
