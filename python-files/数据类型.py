"""
进制种类    引导符号
十进制        无
二进制      0b或0B
八进制      0o或0O
十六进制    0x或0X
"""

# pow(x , y)  计算x的y次方
print(pow(2, 100))
print(pow(2, pow(5, 2)))


# 浮点数类型与整数类型由计算机的不同硬件单元执行，处理方法不同，0.0与0值相同但在计算机内部表示不同
import sys
print(sys.float_info)
print(sys.float_info.max)

a = float(pow(2, 15))
print(pow(pow(2, 3), 5))
