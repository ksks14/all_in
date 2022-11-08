#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 2:55   lbs      1.0         None
"""


class BaseLinaerSearch:
    def __init__(self):
        pass

    def linear_seek(
            self,
            Line: list,
            val,
    ):
        """
        顺序查找 时间复杂度：O(n)
        :param Line:
        :param val:
        :return:
        """
        for key, value in Line:
            if value == val:
                return key
        return None
