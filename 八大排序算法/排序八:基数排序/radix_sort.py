#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/3 12:09 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : radix_sort.py
import copy
import random
from typing import List


def radix_sort(l: List) -> List:
    """
    基数排序
    1.将所有带比较的数值统一为一样的数位长度，数位短的前面补零
    2.从最低位开始，按照最低位数的大小将数放进 0 到 9 的 10 个桶中
    3.按照从 0 到 9 的顺序取出书，同一个桶中的数，按照先进先出的顺序取出
    4.从最低位到最高位依次排序完取出之后，序列就是有序序列了
    :param l: 原序列
    :return: 有序序列
    """
    m = l[0]  # 序列中的最大值
    for i in l:  # 获取序列中的最大值
        if i > m:
            m = i

    n = len(str(m))  # 获取最大值得位数

    i = 0  # 位数，0 表示个位
    while i <= n:  # 遍历 0 到 n 位
        tmp = [[] for _ in range(10)]  # 初始化 10 个桶，每个桶都是一个列表
        for each in l:
            tmp[(each // 10 ** i) % 10].append(each)  # 将每个数先降级再获取第 i 位的数，将该数存放在第 i 个桶中
        l.clear()  # 清空列表
        for x in tmp:  # 遍历 0 到 9 ，共 10 个桶
            for y in x:  # 遍历每个桶里的数，一次取出（按照索引，遵循先进先出）
                l.append(y)
        i += 1
    return l


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
    for i in range(10):
        p.append(random.randint(0, m))
    return p


def main():
    k = gen(1000)
    print(f'start: {k}')
    result = radix_sort(k)
    print(f'result: {result}')
    result1 = bubble_sort(copy.deepcopy(k))
    print(f'result1: {result1}')
    if result1 != result:
        print('错误')
        raise
    else:
        print('正确')


if __name__ == '__main__':
    for i in range(1000):
        main()
