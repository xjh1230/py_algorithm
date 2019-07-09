# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 14:00
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : search_matrix.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/search-a-2d-matrix/
        编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        '''
        pass

    def searchMatrix(self, matrix, target: int) -> bool:
        index_x = -1
        if len(matrix) == 0: return False
        if len(matrix[0]) == 0: return False
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            index_x = i
        if index_x < 0:
            return False
        for j in range(len(matrix[index_x])):
            if matrix[index_x][j] == target:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    t = 32
    print(s.searchMatrix(m, t))
