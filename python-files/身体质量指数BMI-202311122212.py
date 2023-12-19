height, weight = eval(input("请输入升高(米)体重(kg)，用逗号隔开"))
bmi = weight / height**2
print("bim为：{:.2f}".format(bmi))
if bmi < 18.5:
    who, dom = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, dom = "正常", "正常"
elif 24 <= bmi < 25:
    who, dom = "正常", "偏胖"
elif 25 <= bmi <= 28:
    who, dom = "偏胖", "偏胖"
elif 28 <= bmi <= 30:
    who, dom = "偏胖", "肥胖"
else:
    who, dom = "肥胖", "肥胖"
print("国际{}，国内{}".format(who, dom))
