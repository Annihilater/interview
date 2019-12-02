#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/30 10:40 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : bubble_sort.py
import random
import time
from typing import List


def bubble_sort(l: List) -> List:
    """
    冒泡排序（升序）
    :param l:源数组
    :return:排序后的数组
    """
    if len(l) == 0 or len(l) == 1:
        return l

    for i in range(len(l) - 1):
        changed = False
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                changed = True
        if not changed:  # 如果遍历一次，没有发生调换，则说明数组是有序的
            return l

    return l


def main():
    n = []
    m = 1000
    for i in range(m):  # 生成随机数组
        n.append(random.randint(0, m))
    start = time.perf_counter()
    result = bubble_sort(n)
    print(result)
    print(time.perf_counter() - start)


if __name__ == '__main__':
    main()
