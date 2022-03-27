#!/usr/bin/env python3
# coding: utf-8

import math


def format_min_value(x):
    """
    :param x: 列表中最小值
    :return: 返回结果为最小值最终的取整结果即：min_value
    """
    """
            判断min_value的位数
                如果是一位：min_value除以10，再向下取整
                如果是两位：min_value除以100，再向下取整
                如果是三位：min_value除以1000，再向下取整
                以此类推。。。
    """
    min_value = math.floor(x)

    i = len(str(min_value))  # 取出min_value的位数

    if i == 1:
        min_value = math.floor(min_value / 10)
    elif i == 2:
        min_value = math.floor(min_value / 100)
    elif i == 3:
        min_value = math.floor(min_value / 1000)
    # print("最小值向下取整：", min_value)
    return min_value


def format_max_value(y):
    """
    :param y:列表中最大值
    :return:返回结果为最小值最终的取整结果即：max_value
    """
    """
            判断max_value的位数
                如果是两位：max_value除以10，向上取整后再乘以10
                如果是三位：max_value除以100，向上取整，再乘以100
                如果是四位：max_value除以1000，向上取整，再乘以1000
                以此类推。。。
    """
    max_value = math.ceil(y)

    j = len(str(max_value))  # 取出min_value的位数

    if j == 2:
        max_value = math.ceil(max_value / 10) * 10
    elif j == 3:
        max_value = math.ceil(max_value / 100) * 100
    elif j == 4:
        max_value = math.ceil(max_value / 1000) * 1000
    # print("最大值向上取整：", max_value)

    return max_value
