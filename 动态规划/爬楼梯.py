#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/18 16:11
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 爬楼梯.py
import time


def F(n):
    """
    有一座高度是 10 级台阶的楼梯，从下往上走，每跨一步只能向上 1 级或者2 级台阶。要求使用程序来求出一共有多少种走法？
    :param n:总台阶数
    :return: 到达 n 台阶的方法数
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(3, n):
            a, b = b, a + b
        return a + b


if __name__ == '__main__':
    start = time.perf_counter()
    ways = F(3)
    print(ways)
    print(time.perf_counter() - start)
