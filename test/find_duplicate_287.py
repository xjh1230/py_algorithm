#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/10/1 12:46
# @Software: PyCharm
# @File    : find_duplicate_287.py


class Solution:
    def __init__(self):
        """
        https://leetcode-cn.com/problems/find-the-duplicate-number/
        给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def findDuplicate1(self, nums) -> int:
        '''
        快慢指针法
        :param nums:
        :return:
        '''
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow

    def findDuplicate(self, nums) -> int:
        '''
        二分法
        :param nums:
        :return:
        '''
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            mid = int(start + (end - start) / 2)
            c = 0
            for i in nums:
                if i <= mid:
                    c += 1

            if c > mid:
                end = mid
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 4, 2, 2]
    res = s.findDuplicate(arr)
    res1 = s.findDuplicate1(arr)
    print(res, res1)
