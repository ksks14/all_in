#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 2:49   lbs      1.0         None
"""
from TimeUtils.code_time import get_process_time


class BaseBinarySearch:
    def __init__(self):
        pass

    @classmethod
    @get_process_time
    def base_search(cls, L: list, val):
        """
        二分查找要求序列必须是有序的。
        :param L:
        :param val:
        :return:
        """
        left, right = 0, len(L) - 1
        while left <= right:
            mid = (left + right) // 2
            if L[mid] == val:
                return mid
            elif L[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        return None
