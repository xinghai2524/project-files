import random
a = 2
prize = 0
for i in range(10000000):
    door_number = random.randint(1, 3)
    if door_number in [1, 2]:   # 选1、2号门，就可以提车，不换就可以提羊
        if a == 2:
            prize += 1
    else:
        if a == 1:
            prize += 1
print("{}换,机率为{}%".format(a, prize / 100000))
