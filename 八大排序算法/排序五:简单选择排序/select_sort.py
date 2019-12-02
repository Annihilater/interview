#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/2 11:27 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : select_sort.py
import copy
import random
from typing import List


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


def gen(m: int) -> List:
    """
    生成长度为 m ，所以元素在 0 - m 之间的随机序列
    :param m: int
    :return: 随机序列
    """
    k = []
    for i in range(m):
        k.append(random.randint(0, m))
    return k


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
    k = gen(10)
    print(f'start: {k}')
    result = select_sort(k)
    result1 = bubble_sort(copy.deepcopy(k))
    print(f'result:  {result}')
    print(f'result1:  {result1}')
    if result == result1:
        print('正确')
    else:
        print('错误')
        raise


if __name__ == '__main__':
    for i in range(1000):
        main()
