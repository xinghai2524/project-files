import turtle
turtle.speed(0)
turtle.setup(0.5, 0.5, None, None)
turtle.colormode(255)
turtle.pencolor(0, 0, 0)
turtle.pensize(25)
turtle.up()
turtle.forward(-300)
turtle.down()
turtle.seth(-40)
a = 255
for i in range(4):
    for e in range(20):
        turtle.pencolor(255, a, a)
        turtle.circle(40, 4)
        a = a - 1
    for b in range(20):
        turtle.pencolor(255, a, a)
        turtle.circle(-40, 4)
        a = a - 1
for e in range(10):
    turtle.pencolor(255, a, a)
    turtle.circle(40, 4)
    a = a - 1
for e in range(10):
    turtle.pencolor(255, a, a)
    turtle.forward(2.8)
    a = a - 1
for e in range(18):
    turtle.pencolor(255, a, a)
    turtle.circle(16, 10)
    a = a - 1
for e in range(10):
    turtle.pencolor(255, a, a)
    turtle.forward(2.8)
    a = a - 1
turtle.done()
