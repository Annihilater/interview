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


def insert_sort(l: List) -> List:
    if len(l) == 0 or len(l) == 1:
        return l
    for i in range(len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
    return l


def verify(func):
    for i in range(10000):
        k = []
        m = 10
        for i in range(10):
            k.append(random.randint(0, m))
        # print(f'start: {k}')
        start = time.perf_counter()
        result1 = func(k)
        # print(f'result: {result1}')
        result2 = insert_sort(copy.deepcopy(k))
        if result1 != result2:
            print('算法错误')
            raise
        # print(time.perf_counter() - start)
    print('算法正确')


if __name__ == '__main__':
    verify()
