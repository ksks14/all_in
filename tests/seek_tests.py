#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 2:59   lbs      1.0         None
"""
import time
import unittest
from SeekUtils.base_binary_search import BaseBinarySearch
from SeekUtils.base_liner_seek import BaseLinerSearch


class TestSeek(unittest.TestCase):

    @classmethod
    def test_aline_binary_seek(cls, ):
        """

        :return:
        """
        params = {
            'L': [1, 2, 6, 9, 25],
            'val': 6
        }
        res = BaseBinarySearch.base_search(**params)
        assert res == 2

    @classmethod
    def test_aline_liner(cls):
        """

        :return:
        """
        params = {
            'Line': [1, 2, 6, 9, 25],
            'val': 9
        }
        res = BaseLinerSearch.base_search(**params)
        assert res == 3

if __name__ == '__main__':
    unittest.main()
