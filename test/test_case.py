#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/20 16:42
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : test_case.py
import random


def get_test_case():
    s = 'qwertyuiopasdfghjklmnbvcxz'
    length = len(s)
    result = ''
    for i in range(1000000):
        index = random.randint(0, length - 1)
        result += s[index]
    return result


if __name__ == '__main__':
    result = get_test_case()
    print(result)
