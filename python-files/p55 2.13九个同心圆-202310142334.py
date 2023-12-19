import turtle
a, b, c = 5, 0, 30
turtle.pensize(25)
turtle.colormode(255)
for i in range(13):
    turtle.pencolor(150, b, b)
    turtle.circle(a)
    turtle.up()
    turtle.seth(-90)
    turtle.forward(20)
    turtle.seth(0)
    turtle.down()
    a = a + 20
    b = b+c
    c = c-2
turtle.done()
