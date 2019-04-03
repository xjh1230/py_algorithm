# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 11:51
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : merge_intervals.py
# @Software: PyCharm

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/merge-intervals/
        给出一个区间的集合，请合并所有重叠的区间。

        示例 1:

        输入: [[1,3],[2,6],[8,10],[15,18]]
        输出: [[1,6],[8,10],[15,18]]
        解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
        示例 2:

        输入: [[1,4],[4,5]]
        输出: [[1,5]]
        解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
        '''
        pass

    def merge(self, intervals):
        count = len(intervals)
        if count < 2:
            return intervals
        intervals = sorted(intervals, key=lambda s: s.start)
        ret = [intervals[0]]
        for i in intervals:
            tmp = ret.pop()
            if tmp.end >= i.start:
                ret.append(Interval(min(tmp.start, i.start), max(tmp.end, i.end)))
            else:
                ret.append(tmp)
                ret.append(i)
        return ret


if __name__ == '__main__':
    s = Solution()
    li = []
    li.append(Interval(1, 3))
    li.append(Interval(2, 6))
    li.append(Interval(8, 10))
    li.append(Interval(15, 18))

    li = []
    li.append(Interval(1, 4))
    li.append(Interval(4, 5))
    ret = s.merge(li)
    for i in ret:
        print(i.start, i.end)
