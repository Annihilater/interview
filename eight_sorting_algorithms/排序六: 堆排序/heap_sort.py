#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/2 3:18 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : heap_sort.py
from collections import deque
from typing import List

from eight_sorting_algorithms.__init__ import verify


def heap_sort(k: List) -> List:
    """
    堆排序
    1.将序列构造成大根堆（完全二叉树）
    2.遍历二叉树，每次从最大堆内取出最大的数，再调整大根堆
    :param k: 原序列
    :return: 有序序列
    """
    if len(k) < 2:
        return k

    l = deque(k)  # 将原序列转为 deque 对象，可以左边添加元素
    l.appendleft(0)  # 左边补一位 0，因为列表索引的下标是 0 开始，树的索引是 1 开始

    length = len(l) - 1  # 原序列的长度
    count = length // 2  # 所有父节点的个数
    for i in range(count, 0, -1):  # 初始化成大根堆，倒序遍历所有父节点，按照从右向左、从下到上进行逐个调整每个子树，i 就表示父节点
        heap_adjust(l, i, length)  # 起始位：父节点的索引是 i（请看图），结束位：树长 length

    for i in range(length, 0, -1):  # 倒序遍历树，i 就表示末尾子节点，每循环一次，取出一个最大数，再重新调整
        l[1], l[i] = l[i], l[1]  # 将首尾元素调换
        heap_adjust(l, 1, i - 1)  # 起始位：1，结束位：i-1 （减去刚刚抛出的一个节点）
    return list(l)[1:]  # 将 deque 转换为 list，除去第一位（因为手动添加了）返回


def heap_adjust(l: deque, start: int, end: int) -> None:
    """
    原地调整堆结构，使之成为大根堆，不需要返回
    :param l: 堆
    :param start: 调整的起始位置
    :param end: 调整的结束位置
    :return:
    """
    i = start  # i 表示一个父节点
    j = 2 * i  # 父节点的左子节点
    while j <= end:
        if j < end and l[j] < l[j + 1]:  # 如果左子节点小于右子节点，就执行 j=j+1 这样 j 就表示的就是最大的子节点了
            j += 1
        if l[j] > l[i]:  # 如果较大的子节点大于父节点，就将两者调换，再向下继续调整
            l[i], l[j] = l[j], l[i]

            i = j  # 把当前的子节点作为父节点
            j = 2 * i  # j 表示左子节点，在不超出树范围的情况下，重复以上操作
        else:  # 如果最大子节点都小于父节点，说明这个父节点对应的子树顺序正确，调整完毕退出循环
            break


if __name__ == '__main__':
    verify(heap_sort)
