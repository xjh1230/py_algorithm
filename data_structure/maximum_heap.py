#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/12/23 16:30
# @Software: PyCharm
# @File    : maximum_heap.py

class Solution:
    def __init__(self):
        '''

        '''
        self.arr = []
        self.k = 0

    def build_heap(self):
        count = len(self.arr) // 2
        for i in range(count, -1, -1):
            self.heapify(self.arr, len(self.arr), i)

    def heapify(self, arr, heap_size, pos):
        '''
        构建最小堆 跟节点最小，左子树大于右子树
        按照索引排
              0
           1  *  2
         3  4 * 5  6
        :param arr:生成堆的源数组
        :param heap_size: 堆大小 小于等于len(arr)
        :param pos:堆顶点位置
        :return:
        '''
        count, l, r = heap_size, pos * 2 + 1, pos * 2 + 2
        while l < count or r < count:
            largest = l
            if r < count and arr[l] > arr[r]:
                largest = r
            if arr[pos] <= arr[largest]:
                break
            else:
                self.swap(arr, pos, largest)
                pos = largest  # 此时largest为左或右子树，再遍历当前节点的左右子树
                l = pos * 2 + 1
                r = pos * 2 + 2

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def insert(self, val):
        if self.arr[0] < val:
            self.arr[0] = val
            self.build_heap()

    def findKthLargest(self, nums, k: int) -> int:
        self.k = k
        self.arr = nums[:k]
        self.build_heap()
        for i in nums[k:]:
            self.insert(i)
        return self.arr[0]


if __name__ == '__main__':
    s = Solution()
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    res = s.findKthLargest(arr, k)
    print(res, s.arr)
