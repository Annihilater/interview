#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/20 10:45
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 最长回文子串.py
from test.test_case import get_test_case


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        返回字符串的最长回文子串
        :param s: 源字符串
        :return: 最长回文子串
        """

        class Record:
            """
            记录索引、回文子串的长度、回文子串的右边界索引
            """

            def __init__(self, index, length, text):
                self.index = index
                self.length = length
                self.rb = index + length  # 右边界索引 right boundary
                self.text = text[self.index - self.length + 1:self.index + self.length] if self.length > 1 else text[
                    self.index]
                self.lps = self.text.replace('#', '')

        def get_record_length(record):
            return record.length

        length = len(s)

        if length == 0:  # 如果是空字符串，则返回空字符串
            return ''

        if length == 1:  # 如果字符串就一个字符，则返回该字符
            return s

        if length == 2:  # 如果字符串是两个字符组成
            if s[0] == s[1]:  # 两字符相同，则返回原字符串
                return s
            else:
                return s[0]  # 两字符不同则，返回第一个字符（当然也可以返回第二个字符）

        if length >= 3:
            records = []
            tmp = '#'.join(s)  # 对原字符串进行预处理
            _length = len(tmp)
            # print(s)  # 测试语句
            # print(tmp)  # 测试语句
            for i in range(_length):  # 以每个字符串为中心遍历，i 表示索引位置
                l = 1  # 每个中新的最小回文子串都为 1
                if i == 0:
                    records.append(Record(i, l, tmp))

                if i > 0:
                    while i - l >= 0 and i + l < _length:  # 回文子串的左右边界的索引必须满足的条件
                        if tmp[i - l] == tmp[i + l]:  # 比较关于中心位置 i 对称的两个字符
                            l += 1
                        else:
                            break
                    records.append(Record(i, l, tmp))

            # for item in records:
            #     print(f'回文串长度：{item.length} 索引：{item.index} 右边界：{item.rb} 字符串:{item.text} 新字符串:{item.lps}')
            records.sort(key=get_record_length, reverse=True)
            # print('排序后：')
            # for item in records:
            #     print(f'回文串长度：{item.length} 索引：{item.index} 右边界：{item.rb} 字符串:{item.text} 新字符串:{item.lps}')

            target = None
            max = 0
            for i in range(len(records)):
                item = records[i]
                if len(item.lps) > max:
                    max = len(item.lps)
                    target = item

            return target.lps


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2 or s == s[::-1]:
#             return s
#         max_len = 1
#         st_index = 0
#
#         for i in range(1, n):
#             even = s[i - max_len: i + 1]
#             odd = s[i - max_len - 1: i + 1]
#
#             if i - max_len - 1 >= 0 and odd == odd[::-1]:
#                 st_index = i - max_len - 1
#                 max_len += 2
#                 continue
#
#             if i - max_len >= 0 and even == even[::-1]:
#                 st_index = i - max_len
#                 max_len += 1
#
#         return s[st_index: st_index + max_len]


def main(s):
    print(f'原始字符串：{s}')
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(f'最长回文子串：{result}')
    print('\t')


if __name__ == '__main__':
    # s = 'cabadabae'
    # s = 'babad'
    # s = 'ac'
    # s = 'ccc'
    # s = 'abb'
    s = 'cbbd'
    s_list = ["abcdcef",
              "adaelele",
              "cabadabae",
              "aaaabcdefgfedcbaa",
              "aaba",
              "aaaaaaaaa"]
    # for item in s_list:
    #     main(item)
    main(get_test_case())
