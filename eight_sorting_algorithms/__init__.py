#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/18 6:03 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : __init__.py
import copy
import random
import time
from typing import List


def bubble_sort(l: List) -> List:
    if len(l) == 0 or len(l) == 1:
        return l
    for i in range(len(l) - 1):
        changed = False
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                changed = True
        if not changed:
            return l
    return l


def insert_sort(l: List) -> List:
    if len(l) == 0 or len(l) == 1:
        return l
    for i in range(len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
    return l


def verify(func):
    """
    随机生成长度的 10 的序列校验排序算法的正确性，共校验 10000 次
    1.使用直接插入算法校验其他算法
    2.使用冒泡排序算法校验直接插入算法
    :param func: 待校验的排序算法
    :return:
    """
    if func.__name__ == 'insert_sort':
        verify_func = eval('bubble_sort')
        print('Using bubble_sort verify.')
    else:
        verify_func = eval('insert_sort')
        print('Using insert_sort verify.')

    for i in range(10000):
        k = []
        m = 10000
        for i in range(10):
            k.append(random.randint(0, m))
        # print(f'start: {k}')
        start = time.perf_counter()
        result1 = func(k)
        result2 = verify_func(copy.deepcopy(k))

        # print(f'result1: {result1}')
        # print(f'result2: {result2}')

        if result1 != result2:
            print('The algorithm is wrong!!!')
            raise
        # print(time.perf_counter() - start)
    print('The algorithm is correct!!!')


if __name__ == '__main__':
    verify(insert_sort)
