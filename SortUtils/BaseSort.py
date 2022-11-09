#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 3:54   lbs      1.0         None
"""
import copy

"""
该文件包含
1. 冒泡排序 每一趟可以把最大的挪到顶端
2. 选择排序 剔除掉冒泡排序中无用的排序
3. 插入排序 每一次排序都插入到对应的位置
"""
from TimeUtils.code_time import get_process_time


class BaseBubbleSort:
    def __init__(self):
        pass

    @classmethod
    @get_process_time
    def a_line_sort(cls, line: list, flag: bool):
        """
        冒泡排序
        :param line:
        :param flag: True: 顺序, False: 倒序
        :return:
        """
        for i in range(len(line) - 1):
            exchange = False
            for j in range(len(line) - i - 1):
                if flag:
                    if line[j] > line[j + 1]:
                        line[j], line[j + 1] = line[j + 1], line[j]
                        exchange = True
                else:
                    if line[j] < line[j + 1]:
                        line[j], line[j + 1] = line[j + 1], line[j]
                        exchange = True
            if not exchange:
                break


class SelectSort:
    def __init__(self):
        pass

    @classmethod
    @get_process_time
    def a_line_sort(cls, line: list, flag: bool):
        """
        选择排序：减去冒泡排序无效的交换
        min()方法O(n)
        remove()方法O(n)
        :param line:
        :param flag:
        :return:
        """
        for i in range(len(line) - 1):
            flag_index = i
            for j in range(i + 1, len(line)):
                if flag:
                    if line[j] < line[flag_index]:
                        flag_index = j
                else:
                    if line[j] > line[flag_index]:
                        flag_index = j
            if flag_index != i:
                line[flag_index], line[i] = line[i], line[flag_index]


class InsertSort:
    def __init__(self):
        pass

    @classmethod
    @get_process_time
    def a_line_sort(cls, line: list, flag: bool):
        """

        :param line:
        :param flag:
        :return:
        """
        for i in range(1, len(line)):
            temp = line[i]
            j = i - 1
            while j >= 0:
                if flag and line[j] > temp:
                    line[j + 1] = line[j]
                    j -= 1
                elif not flag and line[j] < temp:
                    line[j + 1] = line[j]
                    j -= 1
            line[j + 1] = temp
