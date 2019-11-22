#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/21 19:47
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 动态规划方法.py


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s

        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res


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
