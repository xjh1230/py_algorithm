# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 11:05
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : subsets_ii.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/subsets-ii/
        给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

        说明：解集不能包含重复的子集。

        示例:

        输入: [1,2,2]
        输出:
        [
          [2],
          [1],
          [1,2,2],
          [2,2],
          [1,2],
          []
        ]
        '''

    def subsetsWithDup1(self, nums):
        nums.sort()
        temp = [[]]
        for i in nums:
            tmp = temp.copy()
            print(tmp)
            for p in tmp:
                p = [i] + p
                temp.append(p)
        temp.sort()
        j = 0
        while j < len(temp):
            if j != 0 and temp[j] == temp[j - 1]:
                temp.pop(j)
            else:
                j += 1
        return temp

    def subsetsWithDup2(self, nums):
        res = [[]]
        nums.sort()
        for i in nums:
            tmp = [j for j in res]
            for t in tmp:
                res.append([i] + t)
        res.sort()
        cur, tmp = res[0], [res[0]]
        for i in res:
            if i != cur:
                tmp.append(i)
                cur = i
        return tmp

    def subsetsWithDup(self, nums):
        res = []

        def get(li, cur):
            res.append(cur)
            pre = None
            for i in range(len(li)):
                if li[i] != pre:  # 保证每次新增不会有重复元素
                    get(li[i + 1:], cur + [li[i]])
                pre = li[i]

        nums.sort()
        get(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    li = [1, 2, 2]
    res = s.subsetsWithDup(li)
    print(res)
