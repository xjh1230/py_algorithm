# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 11:53
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : permutations_ii.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        给定一个可包含重复数字的序列，返回所有不重复的全排列。
        https://leetcode-cn.com/problems/permutations-ii/
        '''
        pass

    def permuteUnique1(self, nums):
        li = list()
        li.append(nums)
        for i in range(len(nums)):
            tmp = self.gen(li, i)
            # print(tmp)
            li.extend(tmp)
        li = list(set([tuple(t) for t in li]))
        li = list(list(t) for t in li)
        return li

    def gen(self, lis, start):
        result = []
        for li in lis:
            for i in range(start, len(li)):
                if li[start] != li[i]:
                    tmp = list(li)
                    result.append(self.swap(tmp, start, i))
        return result

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        return nums

    def permuteUnique(self, nums):
        ret = []
        unique = set()
        que = []
        for i, num in enumerate(nums):
            if num not in unique:
                unique.add(num)
                que.append(([num], {i}))
        n = len(nums)
        while que:
            arr, used = que.pop()
            if len(arr) == n:
                ret.append(arr)
            else:
                unique = set()
                for i, num in enumerate(nums):
                    if i not in used and num not in unique:
                        que.append((arr + [num], {i} | used))
                        unique.add(num)
        return ret





if __name__ == '__main__':
    # s = Solution()
    # result = s.permuteUnique([1, 1, 1, 2])
    # print(result)
    s = Solution1()
    print(s.numSquares(6))
