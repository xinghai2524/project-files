import time
n = input("请输入你的名字：")
time.sleep(2)
print("正在请求计算")
time.sleep(5)
for e in range(1,4):
    h = "." * e
    print("\r正在连接{}".format(h),end = "")
    time.sleep(1.6)
print()

print("连接成功，正在计算")
time.sleep(0.1)

c = 0
for i in range(0,101):
    
    
    a = int(((i / 100) ** 6) * 100)
    b = "*" * a
    c = "." * (100 - a)
    print("\r{:>3}% {}->{}".format(a,b,c),end ="")
    time.sleep(0.05)

print()
print("计算成功，正在获取输出结果")
time.sleep(3)
print("获取成功，你的名字是：{}".format(n))
time.sleep(6)
