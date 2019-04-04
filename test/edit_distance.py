# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 16:47
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : edit_distance.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        Levenshtein Distance算法
        https://www.cnblogs.com/sumuncle/p/5632032.html
        https://mp.weixin.qq.com/s?__biz=MjM5MTYwMjI3Mw==&mid=2652097703&idx=1&sn=ba293c267fda9629bb41eaf6fb4bfc89&chksm=bd546fa98a23e6bf5baaf888596f7fadef3b883e022921a5fe1563c5f1da2425ef72b844497b&scene=0&xtrack=1&key=60f932dd5bc68039014180b741c41c59b6e5aa51b976d139e76f0a37931f59a70d43e89b8587b5c09f53689619218cecff6a9c0fd943c75c9cac899ec93cdbf61dcf8212503be7f1463fc1c84dc4be6a&ascene=1&uin=MTg4Njc3MTc2MA%3D%3D&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=k6vNurw8LWlL%2Bsn4Cpk%2F7ZPfY1vJr%2BCgUQ%2F9gP7jLlkGu9sALwv9jDu4tj%2BJeU3Q
        https://leetcode-cn.com/problems/edit-distance/
        给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

        你可以对一个单词进行如下三种操作：

        插入一个字符
        删除一个字符
        替换一个字符
        示例 1:

        输入: word1 = "horse", word2 = "ros"
        输出: 3
        解释:
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')
        dp(dynamic programming)实现
        https://mp.weixin.qq.com/s?__biz=MjM5MTYwMjI3Mw==&mid=2652097703&idx=1&sn=ba293c267fda9629bb41eaf6fb4bfc89&chksm=bd546fa98a23e6bf5baaf888596f7fadef3b883e022921a5fe1563c5f1da2425ef72b844497b&scene=0&xtrack=1&key=60f932dd5bc68039014180b741c41c59b6e5aa51b976d139e76f0a37931f59a70d43e89b8587b5c09f53689619218cecff6a9c0fd943c75c9cac899ec93cdbf61dcf8212503be7f1463fc1c84dc4be6a&ascene=1&uin=MTg4Njc3MTc2MA%3D%3D&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=k6vNurw8LWlL%2Bsn4Cpk%2F7ZPfY1vJr%2BCgUQ%2F9gP7jLlkGu9sALwv9jDu4tj%2BJeU3Q
        没看懂
        '''
        pass

    def minDistance1(self, word1: str, word2: str) -> int:
        # 初始化matrix第一行为0到n，第一列为0到m。
        # Matrix[0][j]表示第1行第j-1列的值，这个值表示将串s[1…0]转换为t[1..j]所需要执行的操作的次数，
        # 很显然将一个空串转换为一个长度为j的串，只需要j次的add操作，所以matrix[0][j]的值应该是j，
        # 其他值以此类推。
        m, n = len(word1), len(word2)
        matrix = [[0 for i in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            matrix[i][0] = i
        for i in range(n + 1):
            matrix[0][i] = i#0
        for i in range(1, m + 1):
            tmp_a = word1[i - 1]
            for j in range(1, n + 1):
                tmp_b = word2[j - 1]
                if tmp_a == tmp_b:
                    tmp_count = 0
                else:
                    tmp_count = 1
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + tmp_count)
        # print(m, n)
        for i in matrix:
            print(i)
        return matrix[m][n]

    def minDistance(self, word1, word2):
        ret = [{} for _ in range(len(word1) + 1)]

        def getDistance(i, j):
            # print(i, j)
            # if i == 0: return j
            # if j == 0: return i
            if i * j == 0: return i + j
            if j in ret[i]:
                return ret[i][j]
            if word1[i - 1] == word2[j - 1]:
                distance = getDistance(i - 1, j - 1)
            else:
                distance = min(getDistance(i, j - 1), getDistance(i - 1, j - 1), getDistance(i - 1, j)) + 1
            ret[i][j] = distance
            return distance

        return getDistance(len(word1), len(word2))


if __name__ == '__main__':
    s = Solution()
    # print(s.minDistance1('intention', 'execution'))
    print(s.minDistance1('annual', 'annealing'))
