#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/2 11:27 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : select_sort.py
from typing import List

from eight_sorting_algorithms.__init__ import verify


def select_sort(l: List) -> List:
    """
    简单选择排序
    1.遍历序列
    2.第 i 次遍历选出最小数，与第 i 位置上的数交换
    :param l:
    :return:
    """
    if len(l) < 2:
        return l

    for i in range(len(l)):  # 遍历序列
        for j in range(i + 1, len(l)):  # 从 i+1 位往后，找出最小数，放到 i 位置上
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l


if __name__ == '__main__':
    verify(select_sort)
