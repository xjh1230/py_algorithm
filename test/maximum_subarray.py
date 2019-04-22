# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 16:58
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : maximum_subarray.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/maximum-subarray/
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

        示例:

        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
        '''

    def maxSubArray1(self, nums) -> int:
        if len(nums) < 1:
            return 0
        dp = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            dp.append(nums[i] + max(0, dp[-1]))
        return max(dp)

    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))
