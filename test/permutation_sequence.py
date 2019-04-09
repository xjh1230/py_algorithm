# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 10:12
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : permutation_sequence.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/permutation-sequence/
        给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

        按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
        给定 n 和 k，返回第 k 个排列。

        说明：

        给定 n 的范围是 [1, 9]。
        给定 k 的范围是[1,  n!]。
        示例 1:

        输入: n = 3, k = 3
        输出: "213"
        '''

    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'
        li_fac = [1]
        li = [str(i) for i in range(1, n + 1)]
        for i in range(2, n):
            li_fac.append(i * li_fac[-1])
        res = []
        for i in range(len(li_fac) - 1, -1, -1):
            a, k = divmod(k, li_fac[i])
            if k == 0:
                res.append(li.pop(a - 1))
                li.reverse()
                res.extend(li)
                break
            elif k == 1:
                res.append(li.pop(a))
                res.extend(li)
                break
            else:
                res.append(li.pop(a))
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4, 4))
