def nums():
    """
    函数用途：将输入的数字转化成列表
    return: i_nums
    """
    a = 1
    i_nums = []
    ip_nums = input("请输入数字1【结束请按回车】")
    while ip_nums != "":
        a += 1
        eval(ip_nums)
        i_nums.append(ip_nums)
        ip_nums = input("请输入数字{}【结束请按回车】".format(a))
    return i_nums


def average(nums_a):
    """
    函数用途：计算平均值
    :param nums_a: 输入数值列表
    :return nums_b: 输出平均值浮点数
    """
    nums_b = 0.0
    for i in nums_a:
        nums_b += eval(i)
    return nums_b / len(nums_a)


def variance(nums_v):
    """
    函数用途：计算方差
    :param nums_v:要计算的数字列表
    :return nums_ar: 方差
    """
    nums_av = average(nums_v)
    nums_ar = 0
    for i in nums_v:
        nums_ar += (eval(i) - nums_av)**2
    return (nums_ar / (len(nums_v) - 1))**0.5


def median(nums_m):
    """
    函数用途：计算中位数
    :param nums_m: 要计算的数字列表
    :return: 输出中位数
    """
    nums_m = sorted(nums_m)
    nums_lm = len(nums_m)
    if nums_lm % 2 == 0:
        return (nums_m[nums_lm/2 - 1] + nums_m[(nums_lm / 2)]) / 2
    else:
        return nums_m[len(nums_m)//2]


print(median(nums()))
