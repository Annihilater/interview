#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/2 10:14 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : merge_sort.py
import copy
import random
from typing import List


def merge_sort(p: List) -> List:
    """
    归并排序，分而治之
    1.分：将序列分成两部分，针对每部分继续分，直到每部分只有一个数
    2.合：将两部分合并，依次比较每部分的首位，将较小的数保存到临时序列
    :param l: 原序列
    :return: 有序序列
    """
    if len(p) < 2:
        return p

    m = len(p) // 2
    l = merge_sort(p[:m])  # 继续分，分到每一部分只有一位数为止
    r = merge_sort(p[m:])
    return merge(l, r)  # 第一次执行merge 的时候：l 是一位数，r 是一位数


def merge(l: List, r: List) -> List:
    """
    将左右部分合并，依次比较两部分的每一个元素，将较小的元素依次添加到临时序列
    :param l: 左序列
    :param r: 右序列
    :return: 合并后的有序序列
    """
    result = []
    i = 0  # 左序列的下标，从 0 开始
    j = 0  # 右序列的下标，从 0 开始
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:  # 依次比较元素，每次添加较小的元素进临时序列
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]  # 右边数已经全部添加完毕，左边还有较大的数剩余
    result += r[j:]  # 左边数已经全部添加完毕，右边还有较大的数剩余
    return result


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


def gen(m: int) -> List:
    p = []
    for i in range(m):
        p.append(random.randint(0, m))
    return p


def main():
    k = gen(10)
    print(f'start: {k}')
    result = merge_sort(k)
    print(f'result: {result}')
    result1 = bubble_sort(copy.deepcopy(k))
    print(f'result1: {result1}')
    if result1 != result:
        print('错误')
        raise


if __name__ == '__main__':
    for i in range(1000):
        main()
