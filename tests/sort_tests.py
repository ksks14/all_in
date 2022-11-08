#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 4:04   lbs      1.0         None
"""
import unittest
from SortUtils.BaseSort import BaseBubbleSort


class TestSort(unittest.TestCase):
    @classmethod
    def test_bubble_sort(cls):
        """

        :return:
        """
        params = {
            'line': [1, 9, 35, 26, 14, 17],
            'flag': True
        }
        res = BaseBubbleSort.a_line_sort(**params)
        assert res == [1, 9, 14, 17, 26, 35]

        params = {
            'line': [1, 9, 35, 26, 14, 17],
            'flag': False
        }
        res = BaseBubbleSort.a_line_sort(**params)
        res.reverse()
        assert res == [1, 9, 14, 17, 26, 35]


if __name__ == '__main__':
    unittest.main()
