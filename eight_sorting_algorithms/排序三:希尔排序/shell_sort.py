#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/1 10:57 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : shell_sort.py
import copy
import random
import time
from typing import List

from eight_sorting_algorithms.lib.verify import verify


def shell_sort(l: List) -> List:
    """
    希尔排序，又称增量缩小排序。
    1.先将数组按照希尔增量进行分组，分别对每组数组进行简单插入排序
    2.缩小增量再次分组，对每组数据进行简单插入排序
    3.直至增量缩小为 1，排序完毕
    :param l:原数组
    :return:有序数组
    """
    n = len(l)
    gap = n // 2  # 增量
    while gap > 0:  # 当 gap = 1 时，下一次的增量就为 0，退出循环
        for i in range(gap, n):  # 对每个分组进行插入排序，因为插入排序是从第二个元素开始的，而此处第二个元素的下标是 gap
            for j in range(i, 0, -gap):  # 控制每个分组内相邻的两个元素，逻辑上相邻的两个元素间距为 gap
                if l[j - gap] > l[j]:  # j 的前一个元素比它少一个 gap 的距离，所以 for 循环中 j 的步长为 -gap
                    l[j - gap], l[j] = l[j], l[j - gap]  # 交换
        gap = gap // 2  # 改变增量
    return l


if __name__ == '__main__':
    verify(shell_sort)
