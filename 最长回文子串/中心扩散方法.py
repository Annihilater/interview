#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/21 16:28
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 中心扩散方法.py


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        max_len = 1  # 至少是 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even  # 当前找到的最长回文子串
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    @staticmethod
    def __center_spread(s: str, size: int, left: int, right: int) -> (str, int):
        """
        left = right 的时候，此时回文中心是间隙，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是字符，回文串的长度是偶数
        :param s:字符串
        :param size:字符串的长度
        :param left:
        :param right:
        :return:
        """
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1


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
