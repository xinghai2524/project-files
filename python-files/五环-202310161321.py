import turtle
turtle.seth(180)
turtle.pensize(15)
a = 116
b = 100
turtle.pencolor("red")
for i in range(5):
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.circle(50)
    a = a - 60
    if b == 100:
        b = 50
    else:
        b = 100

    if i == 0:
        turtle.pencolor("green")
    elif i == 1:
        turtle.pencolor("black")
    elif i == 2:
        turtle.pencolor("yellow")
    else:
        turtle.pencolor("blue")
turtle.done()
