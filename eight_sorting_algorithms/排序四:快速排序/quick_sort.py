#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/1 7:13 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : quick_sort.py
import random
from typing import List

from eight_sorting_algorithms.__init__ import verify


def quick_sort(L: List) -> List:
    return q_sort(L, 0, len(L) - 1)


def q_sort(L: List, left: int, right: int) -> List:
    """
    经典的原地快速排序
    1.先选出基准数，将比基准数小的数放在左边，比基准数大的放在右边
    2.再分别对左右进行快速排序
    :param L: 原序列
    :param left: 最小下标
    :param right: 最大下标
    :return: 有序序列
    """
    if left < right:  # 如果原序列的长度为 0 或者 1 的话，就不满足这个条件，无需排序直接返回原序列
        pivot = partition(L, left, right)
        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L


def partition(L: List, left: int, right: int) -> int:
    """
    找出分组标准，也就是找出基准数，返回基准数的下标
    :param L: 原序列
    :param left: 最小下标
    :param right: 最大下标
    :return: 基准数所在位置的下标
    """
    pivot = L[left]  # 选一个基准数

    while left < right:  # 必须满足左指针小于右指针的条件
        while left < right and L[right] > pivot:  # 右指针向左移，直至遇到小于等于基准数的数
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivot:  # 左指针向右移，直至遇到大于基准数的数
            left += 1
        L[right] = L[left]

    L[left] = pivot
    return left


def simple_quick_sort(l: List) -> List:
    """
    简单版本的快速排序，选择基准数，小于基准数的放在左边，大于基准数的放在右边，在对左右两边进行快排
    :param l: 原序列
    :return:有序序列
    """
    if len(l) < 2:
        return l
    left = [i for i in l[1:] if i <= l[0]]  # 小于等于 a[0] 的数放在左边
    right = [i for i in l[1:] if i > l[0]]  # 大于 a[0] 的数放在右边
    return simple_quick_sort(left) + [l[0]] + simple_quick_sort(right)


if __name__ == '__main__':
    verify(quick_sort)
    verify(simple_quick_sort)
