import turtle
a = 0
while a < 1900:
    if a < 1400:
        turtle.setup(0.5, 0.5, a, 0)
    else:
        a = 0
    a = a + 2
