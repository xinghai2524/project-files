"""
作者：姚星海
作用：货币兑换
时间：2020.08.08
版本：V2.0
版本更新：
   V2.0：函数包装
         修复bug
         增加2种货币
"""


def HL(M):
    USD_DH=6.9579
    EUR_DH=8.2148
    JPY_DH=0.0659
    KRW_DH=0.0059
    HKD_DH=0.8978
    AUD_DH=5.0001

    FH=M[-3:]
    RMB=0

    if M[:-3].isdigit():
        HB = float(M[:-3])
        if FH=='USD'or FH=='usd':
            RMB=HB*USD_DH
        elif FH == 'AUD' or FH == 'aud':
            RMB = float(HB*AUD_DH)
        elif FH == 'HKD' or FH == 'hkd':
            RMB = float(HB*HKD_DH)
        elif FH == 'KRW' or FH == 'krw':
            RMB = float(HB*KRW_DH)
        elif FH=='EUR'or FH=='eur':
            RMB=HB*EUR_DH
        elif FH=='JPY'or FH=='jpy':
            RMB=HB*JPY_DH
        else:
            RMB=-1
    else:
        RMB=-1
    return RMB

def YX():
    M = input('请输入带符号的货币,退出程序请输入‘t’或‘T’')
    i=0
    while M!='T'and M!='t':
        i=i+1
        G=HL(M)
        if G==-1:
            print('格式输入错误,或不支持此货币兑换')
        else:
            print('兑换成人民币为{}元'.format(G))
        M = input('******************************\n请输入带符号的货币,退出程序请输入‘t’或‘T’')

if __name__ =='__main__':
    print('提示：\n 货币   符号 \n 美元   USD \n 港元   HKD \n 韩元   KRW \n 日元   JPY \n 欧元   EUR')
    YX()
    print('已退出程序')
