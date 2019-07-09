# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 15:40
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : max_count.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。

操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。

在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。

示例 1:

输入:
m = 3, n = 3
operations = [[2,2],[3,3]]
输出: 4
解释:
初始状态, M =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

执行完操作 [2,2] 后, M =
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

执行完操作 [3,3] 后, M =
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-addition-ii
        '''

    def maxCount(self, m: int, n: int, ops) -> int:
        li_left = [m]
        li_right = [n]
        if ops and len(ops[0]) > 0:
            for li in ops:
                li_left.append(li[0])
                li_right.append(li[1])
        return min(li_left) * min(li_right)


if __name__ == '__main__':
    s = Solution()
    m, n, ops = 5, 5, [[1, 2], [2, 3]]
    print(s.maxCount(m, n, ops))
