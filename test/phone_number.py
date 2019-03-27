# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 9:19
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : phone_number.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        '''
        self.dic = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                    7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    def letterCombinations2(self, digits):
        if not digits:
            return []
        part = ''
        res = []
        self.dfs(digits, part, res)
        return res

    def dfs(self, nums, part, res):
        if not nums:
            res.append(part)
        else:
            li_tmp = self.dic.get(int(nums[0]))
            for s in li_tmp:
                self.dfs(nums[1:], part + s, res)

    def letterCombinations1(self, digits):
        result = []
        for s in digits:
            if s.isdigit() and 10 > int(s) > 0:
                tmp = self.dic.get(int(s), None)
                if len(result) == 0:
                    result = tmp
                else:
                    result_tmp = result
                    result = []
                    for i in result_tmp:
                        for j in tmp:
                            result.append(i + j)
            else:
                continue
        return result

    def letterCombinations(self, digits):
        if digits == '': return []
        digits.replace('1', '')
        return self.process(digits)

    def process(self, digits):
        li = []
        if digits == '':
            return ['']
        else:
            k = int(digits[0])
            for i in self.dic[k]:
                tmp = self.process(digits[1:])
                for s in tmp:
                    li.append(i + s)
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
