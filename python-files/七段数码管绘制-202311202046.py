import datetime
import turtle


def drawline(draw):     # 绘制单管
    turtle.pendown() if draw else turtle.penup()
    turtle.forward(40)
    turtle.right(90)


def draw_digit(time_digit):     # 绘制七段管
    drawline(1) if time_digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(1) if time_digit in [1, 3, 4, 5, 6, 7, 8, 9, 0] else drawline(False)
    drawline(1) if time_digit in [2, 3, 5, 6, 8, 9, 0] else drawline(False)
    drawline(1) if time_digit in [2, 6, 8, 0] else drawline(False)
    turtle.left(90)
    drawline(1) if time_digit in [4, 5, 6, 8, 9, 0] else drawline(False)
    drawline(1) if time_digit in [2, 3, 5, 6, 7, 8, 9, 0] else drawline(False)
    drawline(1) if time_digit in [1, 2, 3, 4, 7, 8, 9, 0] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.forward(20)


def ta_digit(t_digit):
    turtle.setup(0.8, 0.8, None, None)
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(-400, 0)
    turtle.pendown()
    turtle.seth(0)
    for i in t_digit:
        draw_digit(eval(i))


ta_digit(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
