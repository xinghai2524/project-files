import time
weight = eval(input("请输入您当前的体重"))
rate = 0.5
for i in range(10):
    weight += rate
    time.sleep(0.5)
    print("{}年后您的体重为{:.2f}，在月球的体重为{:.2f}".format(i+1, weight, weight * 0.165))
