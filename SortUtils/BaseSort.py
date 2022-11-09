#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 3:54   lbs      1.0         None

该文件包含
1. 冒泡排序 每一趟可以把最大的挪到顶端
2. 选择排序 剔除掉冒泡排序中无用的排序
3. 插入排序 每一次排序都插入到对应的位置
4. 快速排序 递归排序
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
        :param flag: True: 顺序, False: 倒序
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
        :param flag: True: 顺序, False: 倒序
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


class QuickSort:
    def __init__(self):
        pass

    @classmethod
    def cir_process(cls, line: list, left: int, right: int, flag: bool):
        """
        快速排序最坏的情况，就是列表整个倒序的情况，这样产生的复杂度为O(n*n)，这样有可能会达到递归的最大深度。
        :param flag:
        :param line:
        :param left:
        :param right:
        :return:
        """
        temp = line[left]
        while left < right:
            if flag:
                while left < right and line[right] >= temp:
                    right -= 1
                line[left] = line[right]
                while left < right and line[left] <= temp:
                    left += 1
                line[right] = line[left]
            else:
                while left < right and line[right] <= temp:
                    right -= 1
                line[left] = line[right]
                while left < right and line[left] >= temp:
                    left += 1
                line[right] = line[left]
        line[left] = temp
        return left

    @classmethod
    def a_line_sort(cls, line: list, left: int, right: int, flag: bool):
        """
        递归涉及到了递归的深度问题，并且会很大一部分程度消耗系统的资源。
        :param right:
        :param left:
        :param line:
        :param flag: True: 顺序, False: 倒序
        :return:
        """
        if left < right:
            mid = cls.cir_process(line, left, right, flag)
            cls.a_line_sort(line, left, mid - 1, flag)
            cls.a_line_sort(line, mid + 1, right, flag)

    @classmethod
    @get_process_time
    def base_quick_sort(cls, line: list, flag: bool):
        """
        这里包装的原因是方法需要用到get_process_time作为一个方法装饰器，在递归的过程中，如果将该装饰器加在a_line_sort上，则
        每一次递归调用都会运用该装饰器的方法，这样便完全多余了。
        :param line:
        :param flag: True: 顺序, False: 倒序
        :return:
        """
        cls.a_line_sort(line, 0, len(line) - 1, flag)
