def if_pm(pm):
    if 0 <= pm < 35:
        print("空气质量优，推荐户外运动")
    elif 35 <= pm < 75:
        print("空气质量良好，适度户外运动")
    else:
        print("空气污染，请减少外出")


a = input("请输入pm2.5值")
while a not in ["T", "t"]:
    a = eval(a)
    if_pm(a)
    a = input("请输入pm2.5值")
