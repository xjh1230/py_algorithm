# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 12:44
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : sum_four.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/4sum/
        给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

        注意：

        答案中不可以包含重复的四元组。

        示例：

        给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

        满足要求的四元组集合为：
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
         -> list[list[int]]
         : list[int]
        '''
        pass

    def fourSum(self, nums, target: int):
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        if sum(nums[:4]) > target:
            return res
        for i in range(len(nums) - 3):
            if sum(nums[i:i + 4]) > target:  # 当前元素开始后4位大于target提前退出
                break
            if (i > 0 and nums[i] == nums[i - 1]) or sum(nums[-3:]) + nums[i] < target:
                # 当前元素与前一个元素相当 跳出循环，防止重复
                # 当前循环最后3位+i和小于target 跳出当前循环
                continue
            for j in range(i + 1, len(nums) - 2):
                if j - 1 != i and nums[j] == nums[j - 1]:  # 防止重复
                    continue
                tmp = target - nums[i] - nums[j]
                l, r = j + 1, len(nums) - 1
                if nums[l] > tmp and nums[l] > 0:
                    break
                while l < r:
                    tmp_1 = nums[l] + nums[r]
                    if tmp > tmp_1:
                        l += 1
                    elif tmp < tmp_1:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(s.fourSum([0, 0, 0, 0], 0))
    # print(s.fourSum([-1, 0, 1, 2, -1, -4], -1))
    # print(s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
    # print(s.fourSum([-1, -5, -5, -3, 2, 5, 0, 4], -7))

    print(s.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -9))
