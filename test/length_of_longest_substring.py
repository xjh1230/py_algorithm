# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 9:55
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : length_of_longest_substring.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

        示例 1:

        输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
        '''
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        numer = start = 0
        i = -1
        for i, v in enumerate(s):
            if v in dic:
                numer = max(numer, i - start)
                start = max(dic[v] + 1, start)
            dic[v] = i
        tmp = 0 if i == -1 else i - start + 1
        return max(numer, tmp)

    def lengthOfLongestSubstring1(self, s: str) -> int:
        start = answer = 0
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                start = max(dic[s[i]] + 1, start)
            dic[s[i]] = i
            answer = max(answer, i - start + 1)
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('pwwkew'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('abcdefabc'))
    print(s.lengthOfLongestSubstring('dvdf'))
    print(s.lengthOfLongestSubstring('abba'))
    print(s.lengthOfLongestSubstring(''))
