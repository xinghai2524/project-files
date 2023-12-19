import time
for i in range(1, 101):
    b, c = "*" * i, "." * (100 - i)
    a = i / 100
    g = (i / 100) ** 3
    g = int(g * 100)
    a = int(a * 100)
    b2, c2 = "*" * g, "." * (100 - g)
    time.sleep(0.15)
    print("\r{: ^3.0f}% [{}->{}]\n{: ^3.0f}% [{}->{}]".format(a, b, c, g, b2, c2), end="")
