# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 11:50
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : subarray_sum_equal_k.py
# @Software: PyCharm

class Solution(object):
    def __init__(self):
        '''
        给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        '''

    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = [0] * (len(nums) + 1)
        s = {}
        result = 0
        for (i, v) in enumerate(nums):
            sums[i + 1] = sums[i] + v
            tmp = sums[i + 1] - k
            if tmp in s:
                result += s[tmp]
            if tmp == 0:
                result += 1
            if sums[i + 1] in s:
                s[sums[i + 1]] += 1
            else:
                s[sums[i + 1]] = 1
        return result

    def subarraySum(self, nums, k):
        sum_ = 0
        s = {0: 1}
        res = 0
        for i in nums:
            sum_ += i
            tmp = sum_ - k
            if tmp in s:
                res += s.get(tmp)
            s[sum_] = s.get(sum_, 0) + 1
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [3, 5, 2, -2, 4, 1]
    k = 5
    print(s.subarraySum(arr, k))
    arr = [1, 1]
    k = 0
    print(s.subarraySum(arr, k))
    arr = [0, 1, 1, 1]
    k = 2
    print(s.subarraySum(arr, k))
