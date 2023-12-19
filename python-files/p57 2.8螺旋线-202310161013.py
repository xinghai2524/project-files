import turtle
turtle.colormode(255)
turtle.pensize(15)
a = 2
b = 0
c = 20
while a < 400:
    turtle.pencolor(c,255,c)
    turtle.forward(a)
    turtle.seth(b)
    a = a + 5
    b = b + 90
    c = c + 2
    