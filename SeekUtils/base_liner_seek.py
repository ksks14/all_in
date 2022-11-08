#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 2:55   lbs      1.0         None
"""
from TimeUtils.code_time import get_process_time


class BaseLinerSearch:
    def __init__(self):
        pass

    @classmethod
    @get_process_time
    def base_search(
            cls,
            Line: list,
            val,
    ):
        """
        顺序查找 时间复杂度：O(n)
        :param Line:
        :param val:
        :return:
        """
        for key, value in enumerate(Line):
            if value == val:
                return key
        return None
