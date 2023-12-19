def length(x1, y1, x2, y2):

    import turtle
    turtle.reset()
    length_a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    max_m = abs(max(x1, x2, y1, y2))
    min_a = abs(min(x1, x2, y1, y2))
    max_a = max(max_m, min_a)

    print(max_a)
    if 0 < max_a < 10:
        a = 1
    elif 10 < max_a < 100:
        a = 10
    elif 100 < max_a < 1000:
        a = 100
    elif 1000 < max_a < 10000:
        a = 1000
    elif 10000 < max_a < 100000:
        a = 10000
    else:
        a = 100000

    x1, x2, y1, y2 = x1/a, x2/a, y1/a, y2/a


    max_m = abs(max(x1, x2, y1, y2))
    min_a = abs(min(x1, x2, y1, y2))
    max_a = max(max_m, min_a)

    if max_a < 6:
        c = 59
    else:
        c = 30
    print("两坐标的距离为{:.2f}".format(length_a))

    turtle.setup(0.6, 0.9, None, None)
    turtle.pensize(3)

    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    turtle.seth(0)
    for i in range(2):
        turtle.forward(800)
        if i == 0:
            turtle.up()
            turtle.goto(0, 400)
            turtle.down()
            turtle.seth(-90)
        else:
            i = i
    print(x1, y1, x2, y2)
    turtle.up()
    turtle.goto((x1*c, y1*c))
    turtle.write("({},{})".format(x1 * a, y1 * a))
    turtle.down()
    turtle.goto(x2*c, y2*c)
    turtle.up()
    turtle.write("({},{})".format(x2 * a, y2 * a))


x_2, x_3, x_4 = 'T', 'T', 'T'
x_1 = input("请输入坐标1的x轴数值")
if x_1 not in ['t', 'T']:
    x_2 = input("请输入坐标1的y轴数值")
    if x_2 not in ['t', 'T']:
        x_3 = input("请输入坐标2的x轴数值")
        if x_3 not in ['t', 'T']:
            x_4 = input("请输入坐标2的y轴数值")
            if x_4 not in ['t', 'T']:
                x_1, x_2, x_3, x_4 = x_1, x_2, x_3, x_4
            else:
                x_1 = 'T'
        else:
            x_1 = 'T'
    else:
        x_1 = 'T'
else:
    x_1 = 'T'

while x_1 not in ['t', 'T'] and x_2 not in ['t', 'T'] and x_3 not in ['t', 'T'] and x_4 not in ['t', 'T']:
    if x_1 != '' and x_2 != '' and x_3 != '' and x_4 != '':
        if x_1[0] == '-':
            if x_1[1:].isdigit():
                if x_2[0] == '-':
                    if x_2[1:].isdigit():
                        if x_3[0] == '-':
                            if x_3[1:].isdigit():
                                if x_4[0] == '-':
                                    if x_4[1:].isdigit():
                                        F = 1
                                    else:
                                        F = 0
                                else:
                                    if x_4.isdigit():
                                        F = 1
                                    else:
                                        F = 0
                            else:
                                F = 0
                        else:
                            if x_3.isdigit():
                                F = 1
                            else:
                                F = 0
                    else:
                        F = 0
                else:
                    if x_2.isdigit():
                        F = 1
                    else:
                        F = 0
            else:
                F = 0
        else:
            if x_1.isdigit():
                F = 1
            else:
                F = 0
    else:
        F = 0
    if F == 1:
        x_1, x_2, x_3, x_4 = eval(x_1), eval(x_2), eval(x_3), eval(x_4)
        length(x_1, x_2, x_3, x_4)
    else:
        print("格式输入错误")

    x_1 = input("请输入坐标1的x轴数值")
    if x_1 not in ['t', 'T']:
        x_2 = input("请输入坐标1的y轴数值")
        if x_2 not in ['t', 'T']:
            x_3 = input("请输入坐标2的x轴数值")
            if x_3 not in ['t', 'T']:
                x_4 = input("请输入坐标2的y轴数值")
                if x_4 not in ['t', 'T']:
                    x_1, x_2, x_3, x_4 = x_1, x_2, x_3, x_4
                else:
                    x_1 = 'T'
            else:
                x_1 = 'T'
        else:
            x_1 = 'T'
    else:
        x_1 = 'T'
