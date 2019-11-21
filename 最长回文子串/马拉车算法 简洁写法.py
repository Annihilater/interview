#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/21 10:42
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : 马拉车算法 简洁写法.py


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        马拉车算法
        先在字符串中间加符号隔开，使得奇偶回文数的形式统一
        然后用kmp的思想去优化中心扩散
        :param s: 字符串
        :return: 最长回文子串
        """

        if len(s) == 0:
            return ""
        tmp = '#' + '#'.join(s) + '#'
        # print(tmp) # 测试语句

        mx = 0  # 已遍历的最大右边界
        mid = 0  # 对应的中心点

        l = len(tmp)
        p = [1] * l  # 扩散半径数组，初始值1或者0都可以，只是代表刚开始的时候扩散半径是多少而已

        for i in range(l):
            if i < mx:
                # 这个时候可以用已经计算过的值
                # 不能超过已遍历的右边界
                # i对应的镜像 = 2*mid - i
                # 由mx定义可知半径最长不会超过mx-i
                p[i] = min(mx - i, p[2 * mid - i])

            # 主要的优化已经在上面节省了时间，接下来就是正常的扩散
            while i - p[i] >= 0 and i + p[i] < l and tmp[i - p[i]] == tmp[i + p[i]]:
                p[i] += 1

            if i + p[i] > mx:  # 记录一下mx和mid
                mx = i + p[i]
                mid = i

        maxr = max(p)  # 最长回文的半径
        center = p.index(maxr)  # 最长回文子串的中心
        maxr -= 1  # 因为跳出循环的时候多加了1，所以实际上的扩散半径应该减1

        return tmp[center - maxr:center + maxr + 1].replace('#', "")


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
