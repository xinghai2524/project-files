N = 0
while N < 0.01:
    day_up = 1
    N += 0.001
    for i in range(365):
        if i % 7 in [0, 1, 2, 3, 4]:
            day_up *= (1 + N)
        else:
            day_up = day_up
    print('每天增加{:.1f}%的年终值为{:.4f},一年提高了{:.1f}%'.format(N * 100, day_up, (day_up - 1)*100))

