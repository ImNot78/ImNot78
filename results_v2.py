#!/usr/bin/env python3
# coding: utf-8
import get_values
from format import value_format


def gen_section():
    values_list = get_values.GetValue().get_value_list()
    values_list_1 = list(set(values_list))  # 先使用set把列表转换成集合，再把集合转换成列表，实现列表元素去重
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
        # 调用方法对列表最小值和最大值进行取整
        min_value = value_format.format_min_value(values_list_1[0])  # 最小值
        print("最小值向下取整：", min_value)
        max_value = value_format.format_max_value(values_list_1[len(values_list_1) - 1])  # 最大值
        print("最大值向上取整：", max_value)
        part = (max_value - min_value) / 10  # 算出每个区间间隔的大小
        print("区间间隔是：", part)
        for i in range(1, 11):  # 循环输出每个区间最小和最大值
            a = min_value + part * i
            print(a - part, a)

    elif len(values_list_1) == 1:  # 当前指标数值都相等时，横坐标计算逻辑
        value = value_format.format_max_value(values_list_1[0])
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
