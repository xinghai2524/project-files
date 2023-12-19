def happy(name):
    print("Happy birthday to you\n" * 2, end="")
    print("Happy birthday, dear {}!".format(name))
    print("Happy birthday to you")


happy("n")
print()
happy("Xinghai2524")

"""
程序调用函数需要执行以下4个步骤：
1，调用程序在调用处暂停执行
2，在调用时将实参赋值给函数的参形
3，执行函数体语句
4，函数调用结束返回值，程序回到调用前的暂停处继续执行
"""


def fi():
    f2()


def f2():
    print("000")


fi()

f = lambda x, y: x + y+464646464
print(f(10, 45))


def rpt(str, times=2):
    print(str * times)


rpt("abc")


def vfunc(a, *b):
    print(type(b))
    for i in b:
        a += i
    print(a)
    return a


vfunc(1,2,3,4,5,6,7,8)


def func(x1, x2, y2, z1, z2, y1):
    print("x1={},y1={},x2={},y2={},z1={},z2={}".format(x1, y1, x2, y2, z1, z2))


func(x1=21, y1=31, x2=22, y2=32, z1=41, z2=42)