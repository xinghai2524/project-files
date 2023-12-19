import random
darts = 1000000000
hits = 0
for i in range(1, darts + 1):
    x, y = random.random(), random.random()
    dist = (x ** 2 + y ** 2) ** 0.5
    if dist < 1:
        hits += 1

pi = 4 * (hits / darts)
print(pi)
