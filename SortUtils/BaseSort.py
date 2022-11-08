#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 3:54   lbs      1.0         None
"""
"""
该文件包含
1. 冒泡排序 每一趟可以把最大的挪到顶端
2. 选择排序 插入排序
"""
from TimeUtils.code_time import get_process_time


class BaseBubbleSort:
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
        for i in range(len(line) - 1):
            for j in range(len(line) - i - 1):
                if flag:
                    if line[j] > line[j + 1]:
                        line[j], line[j + 1] = line[j + 1], line[j]
                else:
                    if line[j] < line[j + 1]:
                        line[j], line[j + 1] = line[j + 1], line[j]
        print(line)
        return line
