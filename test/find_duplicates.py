# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 11:34
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : find_duplicates.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
        找到所有出现两次的元素。
        你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
        示例：
        输入:
        [4,3,2,7,8,2,3,1]
        输出:
        [2,3]
        链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
        '''
        pass

    def findDuplicates1(self, nums):
        res = [0] * len(nums)
        s = set()
        for i in range(len(nums)):
            tmp = nums[i] - 1
            res[tmp] = res[tmp] ^ 1
        for i in nums:
            if res[i - 1] == 0:
                s.add(i)
        return list(s)

    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            else:
                res.append(num)
        return res

    def find3(self,nums):
        res = [0] * len(nums)
        li = []
        for n in nums:
            if res[n - 1] == 1:
                li.append(n)
            res[n - 1] += 1
        return li

if __name__ == '__main__':
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    res = s.findDuplicates1(arr)
    print(res)
