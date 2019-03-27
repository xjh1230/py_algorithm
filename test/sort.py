# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 10:34
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : sort.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''

        :param arr:
        '''
        self.count = 0
        pass

    def merge_sort(self, arr):
        import math
        count = len(arr)
        if count < 2:
            return arr
        else:
            mid = math.floor(count / 2)
            l_arr = arr[:mid]
            r_arr = arr[mid:]
            return self.merge(self.merge_sort(l_arr), self.merge_sort(r_arr))

    def merge(self, l_arr, r_arr):
        result = []
        l, r = 0, 0
        while l < len(l_arr) and r < len(r_arr):
            self.count += 1
            l_val, r_val = l_arr[l], r_arr[r]
            if l_val < r_val:
                result.append(l_arr[l])
                l += 1
            else:
                result.append(r_arr[r])
                r += 1
        if l < len(l_arr):
            result.extend(l_arr[l:])
        if r < len(r_arr):
            result.extend(r_arr[r:])
        return result

    def quick_sort(self, arr, left=None, right=None):
        '''
        每次排序，找到一个值做参考，小于放左边，大于放右边
        同样的方法递归左右两边
        :param arr:
        :param left:
        :param right:
        :return:
        '''
        left = left if isinstance(left, (int, float)) else 0
        right = right if isinstance(right, (int, float)) else len(arr) - 1
        if left < right:
            mid = self.partition(arr, left, right)
            self.quick_sort(arr, left, mid)
            self.quick_sort(arr, mid + 1, right)
        return arr

    def partition(self, arr, left, right):
        index = right
        right -= 1
        while left < right:
            self.count += 1
            if arr[left] <= arr[index]:
                left += 1
            else:
                if arr[right] > arr[index]:
                    right -= 1
                else:
                    self.swap(arr, left, right)
        if arr[right] > arr[index]:
            self.swap(arr, right, index)
        return right

    def swap(self, arr, left, right):
        arr[left], arr[right] = arr[right], arr[left]

    def heap_sort(self, arr):
        self.build_heap(arr)
        self.sort_heap(arr)
        return arr

    def build_heap(self, arr):
        count = len(arr) // 2
        for i in range(count, -1, -1):
            self.heapify(arr, len(arr), i)

    def sort_heap(self, arr):
        for i in range(len(arr) - 1):
            self.swap(arr, 0, len(arr) - 1 - i)
            self.heapify(arr, len(arr) - 1 - i, 0)

    def heapify(self, arr, heap_size, pos):
        '''
        构建最大堆 跟节点最大，左子树小于右子树
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
            if r < count and arr[l] < arr[r]:
                largest = r
            if arr[pos] >= arr[largest]:
                break
            else:
                self.swap(arr, pos, largest)
                pos = largest  # 此时largest为左或右子树，再遍历当前节点的左右子树
                l = pos * 2 + 1
                r = pos * 2 + 2

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heap_sort1(self, arr):
        self.build_heap1(arr)
        self.sort_heap1(arr)
        return arr

    def build_heap1(self, arr):
        mid = len(arr) // 2
        for i in range(mid, -1, -1):
            self.heapify1(arr, len(arr) - 1, i)

    def sort_heap1(self, arr):
        size = len(arr) - 1
        for i in range(size):
            self.swap(arr, 0, size - i)
            self.heapify1(arr, size - i, 0)

    def heapify1(self, arr, heap_size, top):
        size, l, r = heap_size, top * 2 + 1, top * 2 + 2
        while l < size or r < size:
            largest = l
            if r < size and arr[l] < arr[r]:
                largest = r
            if arr[top] >= arr[largest]:
                break
            else:
                self.swap(arr, top, largest)
                top = largest
                l = top * 2 + 1
                r = top * 2 + 2


if __name__ == '__main__':
    s = Solution()
    arr = [4, 5, 3, 9, 1, 8, 6, 2, 7, 2, 1]
    s.heap_sort(arr)
    print(arr)
    # arr2 = s.merge_sort(arr)
    # print(arr2, len(arr), len(arr2), s.count)  # 34
    # s.count = 0
    # arr2 = s.quick_sort(arr)
    # print(arr2, len(arr), len(arr2), s.count)  # 62
