#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/19 12:59
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 最长公共子序列.py


def lcs(text1: str, text2: str) -> int:
    d = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]  # 构建空的二维列表，相当于表格

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1])

    # 测试代码：打印 C[i, j] 表格
    # for item in d:
    #     print(item)
    return d[-1][-1]


if __name__ == '__main__':
    s1 = '13456778'
    s2 = '357486782'
    result = lcs(s1, s2)
    print(result)  # 5
