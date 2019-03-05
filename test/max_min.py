# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 14:03
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : max_min.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        self.count = 0

    def get_max_min(self, arr, min_i, max_i):
        if max_i == min_i:
            return (min_i, max_i)
        self.count += 1
        tmp = (min_i + max_i) // 2
        v1 = self.get_max_min(arr, min_i, tmp)
        v2 = self.get_max_min(arr, tmp + 1, max_i)
        max = [v1[1], v2[1]][arr[v1[1]] > arr[v2[1]]]
        min = [v1[0], v2[0]][arr[v1[0]] < arr[v2[0]]]
        return (min, max)

    def get_max_min2(self, arr):
        min_i = max_i = 0
        for i in range(1, len(arr)):
            self.count += 1
            if arr[i] < arr[min_i]:
                min_i = i
            if arr[i] > arr[max_i]:
                max_i = i
        return (min_i, max_i)


if __name__ == '__main__':
    s = Solution()
    arr = [5, 6, 9, 8, 4, 7, 3, 1, 2, 10, 11, 12, 14, 15, 17, 19]
    v = s.get_max_min(arr, 0, len(arr) - 1)

    print(arr[v[0]], arr[v[1]], s.count)
    s.count = 0
    v2 = s.get_max_min2(arr)
    print(arr[v[0]], arr[v[1]], s.count)
