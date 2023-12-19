question = input('退出请输入退出\n加密还是解密？')
while question != '退出':
    if question == '加密':
        plain_code = input("请输入明文：")
        for i in plain_code:
            if ord('a') <= ord(i) <= ord('z'):
                print(chr(ord('a') + (ord(i)-ord('a') + 4) % 26), end='')
            else:
                print(i, end='')
    elif question == '解密':
        cipher_code = input("请输入密文：")
        for j in cipher_code:
            if ord('a') <= ord(j) <= ord('z'):
                print(chr(ord('a') + (ord(j) - ord('a') - 4) % 26), end='')
            else:
                print(j, end='')
    else:
        print('滚！！')
    question = input('\n加密还是解密？')

b = input("好玩吗？\n")
if b == "好玩":
    print("幼稚【狗头】")
elif b == "不好玩":
    print("你爱玩不玩")
else:
    print("哦")
