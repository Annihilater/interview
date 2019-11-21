#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/21 15:11
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 暴力匹配.py
"""
代码没跑通
"""


class Solution:
    # 暴力匹配（超时）
    def longestPalindrome(self, s: str) -> str:
        # 特判
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        # 枚举所有长度大于等于 2 的子串
        for i in range(size - 1):
            for j in range(i + 1, size):
                if j - i + 1 > max_len and self.__valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res

    @staticmethod
    def __valid(s, left, right):
        # 验证子串 s[left, right] 是否为回文串
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


def main(s: str, ans: str) -> None:
    print(f'原字符串：{s}')
    solution = Solution()
    _s = solution.longestPalindrome(s)
    result = True if _s == ans else False
    print(f'是否正确：\033[0;36m{result}\033[0m')
    print(f'正确结果：{ans}')
    print(f'输出结果：{_s}')
    print('\t')


if __name__ == '__main__':
    s_list = ["abcdcef",
              "adaelele",
              "cabadabae",
              "aaaabcdefgfedcbaa",
              "aaba",
              "aaaaaaaaa",
              'adaelele',
              'cbbd',
              'abb',
              'abbb',
              'abbbb',
              'ccd',
              'cccd',
              'ccccd',
              'cbbd']
    answer = ['cdc',
              'elele',
              'abadaba',
              'aabcdefgfedcbaa',
              'aba',
              'aaaaaaaaa',
              'elele',
              'bb',
              'bb',
              'bbb',
              'bbbb',
              'cc',
              'ccc',
              'cccc',
              'bb']
    for i in range(len(s_list)):
        main(s_list[i], answer[i])
