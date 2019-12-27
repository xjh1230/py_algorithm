#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/24 11:33
# @Software: PyCharm
# @File    : find_kth_largest.py

class Solution:
    def __init__(self):
        """
        """
        pass

    def findKthLargest(self, nums, k: int) -> int:
        i = self.quick_sort(nums, 0, len(nums) - 1, k)
        return nums[i]

    def quick_sort(self, nums, l, r, k):
        if l >= r:
            return l
        p = self.partition(nums, l, r)
        if p + 1 == k:
            return p
        if p + 1 < k:
            return self.quick_sort(nums, p + 1, r, k)
        else:
            return self.quick_sort(nums, l, p - 1, k)

    def partition(self, nums, l, r):
        v = nums[l]
        i = l
        l += 1
        while l < r:
            if nums[l] >= v:
                l += 1
            elif nums[r] < v:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
        if nums[l] > v:
            nums[l], nums[i] = nums[i], nums[l]
        return l


class Solution1:
    # 采用快速排序方法，分成的数列左边大于右边
    def findKthLargest(self, nums, k):
        n = len(nums)
        if (k > n):
            return
        index = self.quickSort(nums, 0, n - 1, k)
        print(index)
        return nums[index]

    def quickSort(self, nums, l, r, k):
        if l >= r:
            return l
        p = self.partition(nums, l, r)
        if p + 1 == k:
            return p
        if p + 1 > k:
            return self.quickSort(nums, l, p - 1, k)
        else:
            return self.quickSort(nums, p + 1, r, k)

    def partition(self, nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] >= v:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j


if __name__ == '__main__':
    s = Solution()
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    k = 18
    res = s.findKthLargest(arr, k)
    print(res, arr)
