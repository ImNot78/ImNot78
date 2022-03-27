#!/usr/bin/env python3
# coding: utf-8
import xlrd
import math


class GetValue(object):
    def __init__(self):
        self.value_list = []
        self.path = '/Users/macos/Downloads/testData/指标数值.xls'

    def get_value_list(self):
        read_book = xlrd.open_workbook(self.path)
        read_sheet = read_book.sheet_by_index(0)

        for row in read_sheet.get_rows():
            value_column = row[0]
            value = value_column.value
            self.value_list.append(value)

        self.value_list.sort()
        return self.value_list

    def five_percent_num(self):
        read_book = xlrd.open_workbook(self.path)
        read_sheet = read_book.sheet_by_index(0)

        for row in read_sheet.get_rows():
            value_column = row[0]
            value = value_column.value
            self.value_list.append(value)

        self.value_list.sort()
        """
        1.列表中每个元素所占百分比大于5，则5%分位数 = MIN=a[0]，则5%分位数取a[1]
        2.为了让所有区间边界值都为整数，横坐标显示a[0]和a[1]各自除以8后，a[0]向下取整，a[1]向上取整后，
        再乘以8后的整数。（除以8后取整再乘以8的目的是为了边界值为8个倍数，平均分8份可以整除；
        a[0]向下取整及a[1]向上取整是为了避免两个数都小于8时，可以不得出相同的值）
        """
        if 5 <= 100 / len(self.value_list):
            num00 = math.floor(self.value_list[0] / 8) * 8  # math.floor(x) 向下取整
            num01 = math.ceil(self.value_list[1] / 8) * 8  # math.ceil(x)向上取整
        else:
            num00 = self.value_list[0]
            num01 = math.ceil(self.value_list[1])

        return num00, num01

    def nintyfive_percent_num(self):
        read_book = xlrd.open_workbook(self.path)
        read_sheet = read_book.sheet_by_index(0)

        for row in read_sheet.get_rows():
            value_column = row[0]
            value = value_column.value
            self.value_list.append(value)

        self.value_list.sort()
        """
        95%分位数向下取整确定区间的数组坐标对应值；
        如果当95%分位数 = MAX=a[N-1], 则取a[N-2]。
        为了让所有区间边界值都为整数，横坐标显示a[N-2],，a[N-1]各自除以8后，
        向上取整后，再乘以8后的整数。
        """
        if 95 >= 100 / len(self.value_list) * (len(self.value_list) - 1):
            num02 = math.ceil(self.value_list[len(self.value_list) - 2] / 8) * 8
            num03 = math.ceil(self.value_list[len(self.value_list) - 1] / 8) * 8
        else:
            num02 = math.floor(self.value_list[len(self.value_list) - 2])
            num03 = self.value_list[len(self.value_list) - 1]

        return num02, num03
