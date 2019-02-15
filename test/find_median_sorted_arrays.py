# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 15:41
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : find_median_sorted_arrays.py
# @Software: PyCharm

import math


class Solution:
    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        返回两个数组合并后的中间值，如果合并后个数是奇数的 返回中间数，偶数的，返回 (half+half+1)/2
        """
        m = len(nums1)
        n = len(nums2)
        half = (m + n) / 2
        # new_nums = nums1 + nums2
        new_nums = self.merge_sorted(nums1, nums2)
        print(new_nums)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        if (m + n) % 2 == 0:
            half = int(half)
            return (new_nums[half - 1] + new_nums[half]) / 2
        else:
            return new_nums[math.floor(half)]

    def merge_sorted(self, nums1, nums2):
        '''

        :param nums1:
        :param nums2:
        :return:
        '''
        result = []
        len1 = len(nums1)
        len2 = len(nums2)
        index_1 = 0
        index_2 = 0
        if len1 == 0:
            return nums2
        if len2 == 0:
            return nums1
        if nums1[index_1] > nums2[index_2]:
            result.append(nums2[index_2])
            index_2 += 1
        else:
            result.append(nums1[index_1])
            index_1 += 1
        while index_1 < len1 and index_2 < len2:
            if nums1[index_1] > nums2[index_2]:
                result.append(nums2[index_2])
                index_2 += 1
            else:
                result.append(nums1[index_1])
                index_1 += 1
        if index_1 == len1:
            result.extend(nums2[index_2:])
        else:
            result.extend(nums1[index_1:])
        return result

    def findMedianSortedArrays(self, nums1, nums2):
        '''
        若满足 len(left(nums1)+left(nums2))==len(right(nums1)+right(nums2)) and max(left)<=min(right)
        【即数组已经二分排序，左边都小于右边，且左右两边数量相等】
        则 中位数 为 (max(left)+min(right))/2
        :param nums1:
        :param nums2:
        :return:
        '''
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, math.ceil((m + n) / 2)
        while imin <= imax:
            i = math.floor((imin + imax) / 2)
            j = half_len - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            else:
                if i == 0:
                    max_l = nums2[j - 1]
                elif j == 0:
                    max_l = nums1[i - 1]
                else:
                    max_l = max(nums1[i - 1], nums2[j - 1])
                if (n + m) % 2 == 1:
                    print(max_l, i, j, nums1, nums2)
                    return max_l
                if i == m:
                    min_r = nums2[j]
                elif j == n:
                    min_r = nums1[i]
                else:
                    min_r = min(nums1[i], nums2[j])
                print(max_l, min_r, i, j, nums1, nums2)
                return (max_l + min_r) / 2

    def test(self):
        num1 = [6]
        num1 = [2]
        # num1 = [2, 3, 4, 5]
        num2 = [2, 3, 4, 5, 6, 7, 8]
        # num1 = [1, 2]
        # num2 = [-1, 3]
        print(self.findMedianSortedArrays(num1, num2))
        print(self.findMedianSortedArrays2(num1, num2))
        # print(self.sorted(num1, num2))


if __name__ == '__main__':
    s = Solution()
    s.test()
