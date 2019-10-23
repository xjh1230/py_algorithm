#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/10/23 15:48
# @Software: PyCharm
# @File    : l911_top_voted_candidate.py

import l911_test_data as td
import bisect


class TopVotedCandidate:

    def __init__(self, persons, times):
        '''
        [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]]
        :param persons:
        :param times:
        在选举中，第 i 张票是在时间为 times[i] 时投给 persons[i] 的。
        现在，我们想要实现下面的查询函数： TopVotedCandidate.q(int t) 将返回在 t 时刻主导选举的候选人的编号。
        在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。
        示例：
        输入：["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
        输出：[null,0,1,1,0,0,1]
        解释：
        时间为 3，票数分布情况是 [0]，编号为 0 的候选人领先。
        时间为 12，票数分布情况是 [0,1,1]，编号为 1 的候选人领先。
        时间为 25，票数分布情况是 [0,1,1,0,0,1]，编号为 1 的候选人领先（因为最近的投票结果是平局）。
        在时间 15、24 和 8 处继续执行 3 个查询。
        1 <= persons.length = times.length <= 5000
        0 <= persons[i] <= persons.length
        times 是严格递增的数组，所有元素都在 [0, 10^9] 范围中。
        每个测试用例最多调用 10000 次 TopVotedCandidate.q。
        TopVotedCandidate.q(int t) 被调用时总是满足 t >= times[0]。
        '''
        self.dic = {}
        self.result = {}
        self.max = -1
        self.max_index = -1
        self.li = []
        self.tmp = {}
        for (i, p) in enumerate(persons):
            if p in self.dic:
                self.dic[p] += 1
            else:
                self.dic[p] = 1
            if self.dic[p] >= self.max:
                self.max = self.dic[p]
                self.max_index = p
            self.result[times[i]] = self.max_index
        self.li = list(self.result.keys())

    def q(self, t: int) -> int:
        if t in self.result:
            res = self.result[t]
        elif t in self.tmp:
            res = self.tmp[t]
        else:
            # res = self.result[self.li[self.find(t)]]
            # index = self.find(t)
            index = bisect.bisect(self.li, t) - 1
            res = self.result[self.li[index]]

            self.tmp[t] = res
        return res

    def find(self, t):
        start, end, mid, res = 0, len(self.li), (len(self.li) // 2), 0
        while start < end:
            if self.li[mid] == t:
                return mid
            elif self.li[mid] < t:
                if start == mid:
                    break
                start = mid
            else:
                end = mid
            mid = (end - start) // 2 + start
        res = start
        return res


if __name__ == '__main__':
    print(len(td.p), len(td.t), len(td.q))
    s = TopVotedCandidate(td.p, td.t)
    li = []
    for i in td.q:
        li.append(s.q(i))
    print(li)
