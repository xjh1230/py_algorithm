# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 18:09
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : sum_two.py
# @Software: PyCharm

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, v in enumerate(nums):
            tmp = target - v
            index = dic.get(tmp, -1)
            if index > -1:
                return [i, index]
            else:
                dic[v] = i
        return None


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 6, 7, 5], 9))
