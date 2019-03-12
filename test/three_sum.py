# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 10:26
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : three_sum.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/3sum/
        给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

        注意：答案中不可以包含重复的三元组。
        '''
        pass

    def threeSum(self, nums):
        result = []
        if len(nums) > 2:
            nums.sort()
            for i in range(len(nums) - 2):
                if nums[i] > 0:
                    break
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    tmp = nums[i] + nums[l] + nums[r]
                    if tmp < 0:
                        l += 1
                    elif tmp > 0:
                        r -= 1
                    else:
                        result.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    arr = [-1, 0, 1, 2, -1, -4, 0, 0]
    print(s.threeSum(arr))
    arr = [0, 0, 0]
    print(s.threeSum(arr))

    # print(s.threeSum(arr))
