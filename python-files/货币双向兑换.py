def exchange(money_a, money_b):

    exchange_usd = 7.3060  # 美元
    exchange_rmb = 1.0000  # 人民币
    exchange_jpy = 0.0488  # 日元
    exchange_hkd = 0.9337  # 港币
    exchange_gbp = 8.8727  # 英镑
    exchange_krw = 0.0054  # 韩元
    exchange_eur = 7.6793  # 欧元
    exchange_aud = 4.5969  # 澳元
    exchange_rub = 0.0748  # 俄罗斯卢布
    exchange_thb = 0.2016  # 泰铢
    exchange_twd = 0.2269  # 新台币
    exchange_inr = 0.0877  # 印度卢比
    # 以上信息来源于 百度股市通

    if money_a[:-3].isdigit():
        money_c = float(money_a[:-3])
        if money_a[-3:] in ["USD", "usd"]:
            money_rmb = money_c * exchange_usd
        elif money_a[-3:] in ["RMB", "rmb"]:
            money_rmb = money_c * exchange_rmb
        elif money_a[-3:] in ["JPY", "jpy"]:
            money_rmb = money_c * exchange_jpy
        elif money_a[-3:] in ["HKD", "hkd"]:
            money_rmb = money_c * exchange_hkd
        elif money_a[-3:] in ["GBP", "gbp"]:
            money_rmb = money_c * exchange_gbp
        elif money_a[-3:] in ["KRW", "krw"]:
            money_rmb = money_c * exchange_krw
        elif money_a[-3:] in ["EUR", "eur"]:
            money_rmb = money_c * exchange_eur
        elif money_a[-3:] in ["AUD", "aud"]:
            money_rmb = money_c * exchange_aud
        elif money_a[-3:] in ["RUB", "rub"]:
            money_rmb = money_c * exchange_rub
        elif money_a[-3:] in ["THB", "thb"]:
            money_rmb = money_c * exchange_thb
        elif money_a[-3:] in ["TWD", "twd"]:
            money_rmb = money_c * exchange_twd
        elif money_a[-3:] in ["INR", "tnr"]:
            money_rmb = money_c * exchange_inr
        else:
            money_rmb = "F"
    else:
        money_rmb = "F"

    money_rmb = str(money_rmb)

    if money_rmb not in "F":
        money_rmb = float(money_rmb)
        if money_b in ['USD', 'usd']:
            money_exchange = money_rmb / exchange_usd
            print(money_exchange)
        elif money_b in ['RMB', 'rmb']:
            money_exchange = money_rmb / exchange_rmb
        elif money_b in ['JPY', 'jpy']:
            money_exchange = money_rmb / exchange_jpy
        elif money_b in ['HKD', 'hkd']:
            money_exchange = money_rmb / exchange_hkd
        elif money_b in ['GBP', 'gbp']:
            money_exchange = money_rmb / exchange_gbp
        elif money_b in ['KRW', 'krw']:
            money_exchange = money_rmb / exchange_krw
        elif money_b in ['EUR', 'eur']:
            money_exchange = money_rmb / exchange_eur
        elif money_b in ['AUD', 'aud']:
            money_exchange = money_rmb / exchange_aud
        elif money_b in ['RUB', 'rub']:
            money_exchange = money_rmb / exchange_rub
        elif money_b in ['THB', 'thb']:
            money_exchange = money_rmb / exchange_thb
        elif money_b in ['TWD', 'twd']:
            money_exchange = money_rmb / exchange_twd

        elif money_b in ['INR', 'tnr']:
            money_exchange = money_rmb / exchange_inr
        else:
            money_exchange = "F"
    else:
        money_exchange = "F"

    money_exchange = str(money_exchange)

    if money_exchange in "F":
        print("******************************\n格式输入错误")
    else:
        money_exchange = float(money_exchange)
        print("兑换后的值为：{:.4f}".format(money_exchange))


money_e = input("目录：\nusd,美元  aud,澳元\njpy,日元  hkd,港币\nkrw,韩元  twd,新台币"
                "\neur,欧元  rmb,人民币\nthb,泰铢  inr,印度卢比\ngbp,英镑  rub,俄罗斯卢布\n"
                "格式：100usd\n请输入带符号的货币，退出请输入退出：")
money_f = 0
if money_e != "退出":
    money_f = input("请输入您想兑换的货币的符号：")
else:
    money_e = "退出"


while money_e != "退出" and money_f != "退出":
    exchange(money_e, money_f)
    money_e = input("(查看目录请按t，退出请输入退出)\n请输入您想兑换的货币的符号：")
    while money_e in ['T', 't']:
        print("******************************\n目录：\nusd,美元  aud,澳元"
              "\njpy,日元  hkd,港币\nkrw,韩元  twd,新台币"
              "\neur,欧元  rmb,人民币\nthb,泰铢  inr,印度卢比\ngbp,英镑  rub,俄罗斯卢布\n"
              "格式：100usd")
        money_e = input("请输入带符号的货币，退出请输入退出：")
        money_e = money_e
    if money_e != "退出":
        money_f = input("请输入您想兑换的货币的符号：")
        while money_f in ['T', 't']:
            print("******************************\n目录：\nusd,美元  aud,澳元"
                  "\njpy,日元  hkd,港币\nkrw,韩元  twd,新台币"
                  "\neur,欧元  rmb,人民币\nthb,泰铢  inr,印度卢比\ngbp,英镑  rub,俄罗斯卢布\n"
                  "格式：usd")
            money_f = input("请输入您想兑换的货币的符号：")
    else:
        money_e = "退出"

b = input("好玩吗？\n")
if b == "好玩":
    print("幼稚【狗头】")
elif b == "不好玩":
    print("你爱玩不玩")
else:
    print("哦")
