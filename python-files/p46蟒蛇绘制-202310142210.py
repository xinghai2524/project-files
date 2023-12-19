
def drawsnake(colorstring, width):
    import turtle
    turtle.pensize(width)
    turtle.pencolor(colorstring)
    turtle.up()
    turtle.forward(-300)
    turtle.down()
    turtle.seth(-40)
    for i in range(5):
        turtle.circle(40, 80)
        turtle.circle(-40, 80)
    turtle.circle(40, 40)
    turtle.forward(40)
    turtle.circle(16, 180)
    turtle.forward(40)
    turtle.done()


drawsnake("yellow", 20)
