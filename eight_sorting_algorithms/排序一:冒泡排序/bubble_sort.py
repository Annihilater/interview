#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/30 10:40 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : bubble_sort.py
from typing import List

from eight_sorting_algorithms.__init__ import verify


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


if __name__ == '__main__':
    verify(bubble_sort)
