import time
import turtle
turtle.pensize(25)
scale = 100
for i in range(101):
    turtle.circle(30, 360/100)
    b, c = '*' * i, '.' * (scale - i)
    a = i / scale * 100
    time.sleep(0.1)
    print("\r{:^3.0f}%[{}->{}]".format(a, b, c), end='')
