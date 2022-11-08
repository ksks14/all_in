#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/9 3:30   lbs      1.0         衡量代码的时间
"""
import time
from functools import wraps


def get_process_time(func):
    """

    :param func:
    :return:
    """

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        start = time.process_time()
        func_re = func(*args, **kwargs)
        end = time.process_time()
        res = end - start
        print('CPU Execution time:', res, 'seconds')
        return func_re
    return wrapper_func

