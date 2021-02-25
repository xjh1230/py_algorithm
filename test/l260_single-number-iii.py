#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2021/2/25 16:23
# @Software: PyCharm
# @File    : l260_single-number-iii.py

class find_diff_num:
    def __init__(self):
        """
        """
        pass

    def find_1(self, arr):
        '''
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
        :param arr:
        :return:
        '''
        if len(arr) == 1:
            return arr[0]
        res = arr[0]
        for i in arr[1:]:
            res ^= i
        return res

    def find_2(self, arr):
        '''
        有一个 n 个元素的数组，除了两个数只出现一次外，其余元素都出现两次，让你找出这两个只出现一次的数分别是几，要求时间复杂度为 O(n) 且再开辟的内存空间固定(与 n 无关)。
        :param arr:
        :return:
        '''
        # 第一遍获取找到这两个不一样的元素的异或值
        tmp = self.find_1(arr)
        # 因为这两个只出现一次的元素一定是不相同的，所以这两个元素的二进制形式肯定至少有某一位是不同的，即一个为 0 ，另一个为 1 ，现在需要找到这一位。
        tmp_i = 1
        while True:
            if tmp_i & tmp == tmp_i:
                break
            tmp_i = tmp_i << 1
        # 根据异或的性质 任何一个数字异或它自己都等于 0，得到这个数字二进制形式中任意一个为 1 的位都是我们要找的那一位。
        tmp_1 = 0
        for i in arr:
            if i & tmp_i == tmp_i:
                tmp_1 = tmp_1 ^ i
        tmp_0 = tmp ^ tmp_1
        return [tmp_0, tmp_1]

    def find_3(self, nums):
        nums.sort()
        pre = nums[0]
        appeared = False
        for i in range(1, len(nums)):
            cur = nums[i]
            if pre == cur:
                appeared = True
            else:
                if appeared:
                    pre = cur
                    appeared = False
                else:
                    return pre
        return pre

    def find_3_1(self, nums):
        one = two = 0
        for i in nums:
            # 两次+这次是=3次
            three = two & i
            # 两次+本次不是 或者一次+这次是=2
            two = (two & ~i) | (one & i)
            # 这次是就是奇数次的
            one = one ^ i
            # 移除3次的
            one = one & (~three)
        return one

    def find_3_2(self, nums):
        seen_1 = seen_2 = 0
        for i in nums:
            '''
            第一次出现，添加到seen_one
            第二次出现，移除seen_once,添加seen_twice
            第三次出现，移除seen_twice,并不添加seen_one
            ~seen_2 & num  表示把数从seen_twice移除
            ~seen_1 & num   表示把数从seen_once移除
            第三次出现时，第二次的twice为1，~twice为0，所以once依然为0，第三次的twice=num^num=0，相当于把num从twice中删除
            '''
            seen_1 = ~seen_2 & (seen_1 ^ i)
            seen_2 = ~seen_1 & (seen_2 ^ i)
        return seen_1


if __name__ == '__main__':
    s = find_diff_num()
    arr = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
    print(s.find_3_1(arr))
