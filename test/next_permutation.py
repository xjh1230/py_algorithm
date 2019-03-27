# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 11:28
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : next_permutation.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

        如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

        必须原地修改，只允许使用额外常数空间。

        以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1
        [1,5,8,4,7,6,5,3,1]
        思路：1 从最后往前开始找出  n[i](7)>n[i-1](4)  如果没找到，则说明已经最大，排序当前队列即可
              2 从 i 往后找出最接近[i-1](4) 的值(5)
              3 交换 4，5 位置，同时从 i(7)往后 按大小排序
        '''
        pass

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = len(nums) - 1
        if count > 0:
            min_index = count
            has_max = False
            while count > 0:
                if nums[count] > nums[count - 1]:
                    tmp = count
                    while tmp < min_index:
                        if nums[tmp + 1] > nums[count - 1]:
                            tmp += 1
                        else:
                            break
                    nums[tmp], nums[count - 1] = nums[count - 1], nums[tmp]
                    has_max = True
                    tmp = nums[count:]
                    tmp.sort()
                    nums[count:] = tmp
                    break
                count -= 1
            if not has_max:
                nums.sort()


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    s.nextPermutation(nums)
    print(nums)
