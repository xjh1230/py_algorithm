# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 9:34
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : permutations.py
# @Software: PyCharm

class Solution:
    def __init__(self, is_all=False):
        '''
        生成全排列数据
        '''
        self.count = 0
        # 是否全排列 122 122
        self.is_all = is_all

    def get_dfs(self, str):
        if len(str) == 1:
            return set(str)
        set_result = set()
        for i in range(len(str)):
            set_tmp = self.get_dfs(str[0:i] + str[i + 1:])
            for s in set_tmp:
                # print('第%d次结果:%s' % (self.count, str[i] + s))
                # self.count += 1
                set_result.add(str[i] + s)
        return set_result

    def swap(self, str, index_a, index_b):
        count = len(str)
        if index_a >= count or index_b >= count or index_a == index_b or (self.is_all and str[index_b] == str[index_a]):
            return str
        else:
            if index_a > index_b:
                index_a, index_b = index_b, index_a
            str = str[0:index_a] + str[index_b] + str[index_a + 1:index_b] + str[index_a] + str[index_b + 1:]
        return str





if __name__ == '__main__':
    s = Solution()
    # print(s.swap('1134', 0, 1))
    ss = s.get_dfs('121')
    print(len(ss))
    # sorted(ss)
    for i in ss:
        print(i)
