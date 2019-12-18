#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/30 8:29 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : insert_sort.py
from typing import List

from eight_sorting_algorithms import verify


def insert_sort(l: List) -> List:
    """
    直接插入排序，每次步进一个数，将新数插入到已排序数组的正确位置
    :param l:源数组
    :return:有序数组
    """
    if len(l) == 0 or len(l) == 1:
        return l

    for i in range(1, len(l)):  # 遍历数组，第 i 位是新数，i 之前的是已排序数组
        for j in range(i, 0, -1):  # 针对新数进行插入排序
            if l[j] < l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
            else:
                break
    return l


if __name__ == '__main__':
    verify(insert_sort)
