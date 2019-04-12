# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 15:15
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : minimum_path_sum.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/minimum-path-sum/
        给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

        说明：每次只能向下或者向右移动一步。

        示例:

        输入:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        输出: 7
        解释: 因为路径 1→3→1→1→1 的总和最小。
        '''
        pass

    def minPathSum1(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                # dp[j]前一个元素 dp[j-1]上一个元素
                dp[j] = grid[i][j] + (min(dp[j - 1], dp[j]) or dp[j - 1])
        return dp[-1]

    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(0, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
            for j in range(1, n):
                # (0 or 2) =2  (1 or 2) = 1
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], (dp[i - 1][j] or dp[i][j - 1]))
        for j in dp:
            print(j)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    arr = [[1, 3, 1, 4], [1, 5, 1, 3], [4, 2, 1, 2]]
    # arr = [[1, 2], [5, 6], [1, 1]]
    print(s.minPathSum(arr))
    print(s.minPathSum1(arr))
