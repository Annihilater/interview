#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/20 16:49
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 马拉车算法.py


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pre_handle(s: str) -> str:
            """
            预处理字符串，在字符之间添加特殊符号 #
            注意：首尾也要加上，否则后面寻找最大回文子串中心的时候会出现各种错误
            比如：需要考虑奇偶性等
            :param s: 原字符串
            :return: 新字符串
            """
            sb = '#' + '#'.join(s) + '#'
            return sb

        def find_longest_palindrome_string(s: str) -> str:
            """
            返回字符串的最长回文子串
            :param s: 原字符串
            :return: 最长回文子串
            """
            if not s:
                return ''
            if len(s) == 1:
                return s
            if len(s) == 2:
                if s == s[::-1]:
                    return s
                else:
                    return s[0]

            tmp = pre_handle(s)
            length = len(tmp)

            right_side = 0  # 右边界
            right_side_center = 0  # 右边界的中心
            half_len_arr = [0 for _ in range(length)]  # 保存每个字符为中心回文串长度的一半（向下取整）
            center = 0  # 记录回文中心
            longest_half = 0  # 记录回文长度

            for i in range(length):
                need_calc = True  # 是否需要中心扩展

                if right_side > i:  # 如果字符在右边界覆盖范围内
                    left_center = 2 * right_side_center - i  # 计算 right_side_center 的对称位置
                    half_len_arr[i] = half_len_arr[left_center]  # 右中心的回文长度 = 左中心的回文长度

                    if i + half_len_arr[i] > right_side:  # 如果右中心右边界比中心右边界大，则需要扩展
                        half_len_arr[i] = right_side - i  # 目前以中心的右边界为准

                    if i + half_len_arr[left_center] < right_side:  # 如果右中心右边界小于中心右边界，则不需要扩展
                        need_calc = False

                if need_calc:  # 如果需要扩展

                    while (i - 1 - half_len_arr[i]) >= 0 and (i + 1 + half_len_arr[i]) < length:  # 扩展满足的条件
                        if tmp[i - 1 - half_len_arr[i]] == tmp[i + 1 + half_len_arr[i]]:  # 判断左右字符是否相等
                            half_len_arr[i] += 1
                        else:
                            break

                    right_side = i + half_len_arr[i]  # 更新右边界
                    right_side_center = i  # 更新右边界的中心

                    if half_len_arr[i] > longest_half:  # 记录最长回文子串
                        longest_half = half_len_arr[i]

            # 以下 4 条是测试语句
            # print(tmp)
            # print(f'中心：{center} 半径：{longest_half}')
            # for i in range(length):
            #     print(f'{i} 字符：{tmp[i]} {half_len_arr[i]}')

            longest_half = max(half_len_arr)
            center = half_len_arr.index(longest_half)

            return tmp[center - longest_half:center + longest_half].replace('#', '')

        return find_longest_palindrome_string(s)


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
