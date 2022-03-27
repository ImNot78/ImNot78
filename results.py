#!/usr/bin/env python3
# coding: utf-8
import get_values
import math


def gen_section():
    values_list = get_values.GetValue().get_value_list()
    # 先使用set把列表转换成集合，再把集合转换成列表，实现列表元素去重
    values_list_1 = list(set(values_list))
    values_list_1.sort()
    print(values_list_1)

    if 1 < len(values_list_1) <= 5:  # 当前指标数值小于6个时，横坐标计算逻辑
        """
        横坐标的展示范围随指标值实际分布而定，
        横坐标最小值为指标值最小值向下取整，
        横坐标最大值为指标值最大值向上取整。
        取整的位数=“指标值最大值-指标值最小值”所得的差值的位数。
        在量程范围内，将横坐标最大值到最小值区间十等分，展示10个区间分别的主体个数。
        如果仅一个主体，横坐标最小值设置为0，最大值设置为该主体该指标向上取整，
        取整的位数为该指标值的位数
        """

        """
                判断min_value的位数
                    如果是一位：min_value除以10，再向下取整
                    如果是两位：min_value除以100，再向下取整
                    如果是三位：min_value除以1000，再向下取整
                    以此类推。。。
        """
        # TODO  ：可以将下面的取整方式封装，以后可直接调用
        min_value = math.floor(values_list_1[0])  # 先把最小值向下取整，方便下面取位数
        i = len(str(min_value))  # 取出min_value的位数
        if i == 1:
            min_value = math.floor(min_value / 10)
        elif i == 2:
            min_value = math.floor(min_value / 100)
        elif i == 3:
            min_value = math.floor(min_value / 1000)
        print("最小值向下取整：", min_value)
        max_value = math.ceil(values_list_1[len(values_list_1) - 1])
        """
                判断max_value的位数
                    如果是两位：max_value除以10，向上取整后再乘以10
                    如果是三位：max_value除以100，向上取整，再乘以100
                    如果是四位：max_value除以1000，向上取整，再乘以1000
                    以此类推。。。
        """
        j = len(str(max_value))  # 取出min_value的位数
        if j == 2:
            max_value = math.ceil(max_value / 10) * 10
        elif j == 3:
            max_value = math.ceil(max_value / 100) * 100
        elif j == 4:
            max_value = math.ceil(max_value / 1000) * 1000
        print("最大值向上取整：", max_value)
        part = (max_value - min_value) / 10
        print("区间间隔是：", part)

        for i in range(1, 11):
            a = min_value + part * i
            print(a - part, a)

    elif len(values_list_1) == 1:  # 当前指标数值都相等时，横坐标计算逻辑
        value = math.ceil(values_list_1[0])  # 数值可能是小数，所以先向上取整，得到整数方便后面取位数j
        j = len(str(value))
        print("长度：", j)
        # 取整逻辑参考上面max_value的取整方式即可
        if j == 2:
            value = math.ceil(value / 10) * 10
        elif j == 3:
            value = math.ceil(value / 100) * 100
        elif j == 4:
            value = math.ceil(value / 1000) * 1000
        print("最大值向上取整：", value)
        print("0 - ", value)

    elif len(values_list_1) > 5:  # 当前指标数值多于5个时，横坐标计算逻辑
        nums01 = get_values.GetValue().five_percent_num()
        print("第一个区间是：", nums01)
        nums02 = get_values.GetValue().nintyfive_percent_num()
        # 计算中间的8个区间值
        a = list(nums01)[1]
        b = list(nums02)[0]
        c = (b - a) / 8
        print("区间间隔是：", c)
        for i in range(1, 9):
            d = a + c * i
            print(d - c, d)

        print("末尾区间是：", nums02)


if __name__ == '__main__':
    gen_section()
