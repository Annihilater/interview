#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/18 17:39
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 挖金矿.py
from typing import List


def F(n, w, g: List[int], p: List[int]) -> int:
    """
    问题：有一个国家发现了 5 座金矿，每座金矿的黄金储备量不同，需要挖坑的工人数也不同。参与挖矿工人的总数是 10 人。每座金矿要么全挖，要么不挖，
    不能派出一半人挖取一半金矿。要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取那几座金矿？
    金矿产量数组 g = [400, 500, 200, 300, 350]
    金矿用工数数组 p = [5, 5, 3, 4, 3]
    :param n:金矿数量
    :param w:工人数
    :param g:金矿的黄金量
    :param p:金矿的用工量
    :return:可挖取得最大黄金量
    """
    if n == 0:
        return 0
    if n == 1:
        if w < p[0]:
            return 0
        else:
            return g[0]
    if n > 1:
        if w < p[n - 1]:
            return F(n - 1, w, g, p)
        else:
            return max(F(n - 1, w, g, p), F(n - 1, w - p[n - 1], g, p) + g[n - 1])


if __name__ == '__main__':
    g = [400, 500, 200, 300, 350]
    p = [5, 5, 3, 4, 3]
    result = F(5, 10, g, p)
    print(result)
