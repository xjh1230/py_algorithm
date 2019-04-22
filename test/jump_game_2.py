#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/30 13:37
# software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/jump-game-ii/
        给定一个非负整数数组，你最初位于数组的第一个位置。

        数组中的每个元素代表你在该位置可以跳跃的最大长度。

        你的目标是使用最少的跳跃次数到达数组的最后一个位置。

        示例:

        输入: [2,3,1,1,4]
        输出: 2
        解释: 跳到最后一个位置的最小跳跃数是 2。
             从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
        '''
        pass

    def jump1(self, nums) -> int:
        count = len(nums)
        dic = dict()
        dic[count - 1] = 0
        nums[-1] = -1
        for i in range(count - 2, -1, -1):
            j, num = 1, nums[i]
            tmp = -1
            if num == 0:
                tmp = count - i - 1
            while j <= num:
                if i + j >= count:
                    tmp = 1
                    break
                if nums[i + j] == -1:
                    if tmp == -1:
                        tmp = dic[i + j] + 1
                    else:
                        tmp = min(tmp, dic[i + j] + 1)
                j += 1
            dic[i] = tmp
            nums[i] = -1
        return dic[0]

    def jump2(self, nums) -> int:
        count = len(nums)
        li = [count] * count
        li[count - 1] = 0
        for i in range(count - 2, -1, -1):
            if nums[i] == 0:
                continue
            start = i + 1
            end = min(i + nums[i], count - 1)
            tmp = min(li[start:end + 1])
            li[i] = tmp + 1
        return li[0]

    def jump3(self, nums) -> int:
        reach = 0
        nextreach = nums[0]
        step = 0
        for i in range(len(nums)):
            nextreach = max(i + nums[i], nextreach)
            if nextreach >= len(nums) - 1:
                return step + 1
            if i == reach:
                step += 1
                reach = nextreach
        return step

    def jump4(self, nums) -> int:
        '''
        一次循环跑到最远的
        :param nums:
        :return:
        '''
        step, start, end, far = 0, 0, 0, 0
        while end < len(nums) - 1:
            step += 1
            for i in range(start, end + 1):
                far = max(far, nums[i] + i)
            start, end = end + 1, far
        return step

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        从0开始 找到第一个能1步到终点的位置 n，压栈
        遍历从0 开始 找到1步能到n或者大于n的 m 压栈
        循环 直到0 能入栈

        """
        if len(nums) == 1:
            return 0
        if len(set(nums)) == 1:
            return (len(nums) - 2) // nums[0] + 1
        pos = [len(nums) - 1]
        temp = len(nums) - 1
        count = 0
        while 0 not in pos:
            count += 1
            for j in range(temp):
                if nums[j] + j >= temp:
                    temp = j
                    pos.append(j)
                    break
        return count


import time

if __name__ == '__main__':
    s = Solution()
    # nums = [2, 3, 1, 1, 4]
    # print(s.jump(nums))
    # nums = [2, 3, 0, 1, 4]
    # print(s.jump(nums))
    # nums = [2, 1]
    # print(s.jump(nums))
    # li = [4, 1, 1, 3, 4, 1, 1]
    # print(s.jump(li))
    t = time.time()
    li = [1] * 3000
    print(s.jump(li))
