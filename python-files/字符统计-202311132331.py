str_in = input("请输入字符")
english = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
space = 0
number = 0
else_str = 0
english_str = 0
for i in str_in:
    if i in list("1234567890"):
        number += 1
    elif i in english:
        english_str += 1
    elif i in " ":
        space += 1
    else:
        else_str += 1
print("数字{}个,空格{}个,英文字符{}个,其他字符{}个".format(number, space, english_str, else_str))
