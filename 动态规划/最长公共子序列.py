#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/19 12:59
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 最长公共子序列.py


def lcs(text1: str, text2: str) -> int:
    """
    给定两个字符串 `text1` 和 `text2`，返回这两个字符串的最长公共子序列。
    一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"`ace`" 是 "`abcde`" 的子序列，但 "`aec`" 不是 "`abcde`" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
    若这两个字符串没有公共子序列，则返回 0。
    :param text1:字符串 1
    :param text2:字符串 2
    :return:最长公共子序列的长度
    """
    d = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]  # 构建空的二维列表，相当于表格

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1])

    # 测试代码：打印 C[i, j] 表格
    for item in d:
        print(item)
    return d[-1][-1]


if __name__ == '__main__':
    s1 = '13456778'
    s2 = '357486782'
    result = lcs(s1, s2)
    print(result)  # 5
