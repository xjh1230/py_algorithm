#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2020/7/22 14:14
# @Software: PyCharm
# @File    : l26_remove_duplicate.py

class Solution:
    def removeDuplicates1(self, nums):
        res = 0
        if len(nums) < 2:
            return len(nums)
        i, before, has = 1, nums[res], False
        while i < len(nums):
            if nums[i] <= nums[res]:
                has = True
                j = i
                while j < len(nums):
                    if nums[j] <= nums[res]:
                        j += 1
                    else:
                        nums[res + 1] = nums[j]
                        break
                i = j
                res += 1
            else:
                i += 1
                res += 1
        if has:
            nums[res] = nums[i - 1]
        else:
            res += 1
        return res

    def removeDuplicates2(self, nums) -> int:
        if len(nums) < 1:
            return 0

        new_len = 1
        duplicate_num = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] != duplicate_num:
                nums[new_len] = nums[idx]
                new_len += 1
                duplicate_num = nums[idx]

        return new_len

    def removeDuplicates(self, nums):
        if len(nums) < 1:
            return 0
        res, before = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] != before:
                nums[res] = nums[i]
                res += 1
                before = nums[i]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-3, -3, -2, -1, -1, 0, 0, 0, 0, 0]
    # nums = [1, 1, 2]
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # nums = [0, 0, 0, 0]
    # nums = [1, 2, 3, 4, 5]
    res = s.removeDuplicates(nums)
    print(nums, res)
