#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/18 17:39
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 挖金矿.py
from typing import List


def recursive(n, w, g, p):
    """
    递归解法
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


def F(n, w, g: List[int], p: List[int]) -> int:
    """
    动态规划解法
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
    pre_results = []  # 储存前一次结果，索引是工人数，值是工人数条件下，可挖取的最大黄金量
    results = []  # 储存当前结果，索引是工人数，值是工人数条件下，可挖取的最大黄金量

    for i in range(w + 1):
        workers = p[0]
        if i < workers:  # 只有第一座金矿时，工人数小于用工数，表示不开挖，所得黄金量为 0
            pre_results.insert(i, 0)
        else:  # 开挖时，所得黄金量为第一座金矿黄金量
            pre_results.insert(i, g[0])
    print(pre_results)  # 测试语句：打印查看只有第一座金矿，工人数与可获取的最大黄金量的关系

    for i in range(1, n):  # i 每增加 1 表示，按照金矿的顺序（g 列表）新增一座金矿
        results = []  # 每次遍历都初始化一次 results
        for j in range(w + 1):
            workers = p[i]  # workers 表示新增的这座金矿的用工数
            if j < workers:  # 当工人数小于用工数时，表示新增的这座金矿不开挖
                results.insert(j, pre_results[j])
            else:  # 开挖新增的这座金矿
                tmp = max(pre_results[j], pre_results[j - workers] + g[i])
                results.insert(j, tmp)

        pre_results = results  # 将当前结果保存为上次结果，供下次新增金矿时使用
        print(results)  # 测试语句：每新增加一座金矿，打印查看一次工人数与最大黄金量的关系
    return results[w]


if __name__ == '__main__':
    g = [400, 500, 200, 300, 350]  # 金矿顺序下，各个金矿的含金量列表
    p = [5, 5, 3, 4, 3]  # 金矿顺序下，各个金矿的用工数列表
    result = F(5, 10, g, p)
    print(result)
