#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/10/24 13:16
# @Software: PyCharm
# @File    : l838_push_dominoes.py
import l838_test_data as td


class Effect:
    def __init__(self, status, res):
        self.status = status  # 0静止 1移动 2停止
        self.before = res
        self.cur = res


class Solution:
    def __init__(self):
        '''
        一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。

        在开始时，我们同时把一些多米诺骨牌向左或向右推。
        每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。
        同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
        如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。
        就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。
        给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] = 'R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。
        返回表示最终状态的字符串。

        示例 1：
        输入：".L.R...LR..L.."
        输出："LL.RR.LLRRLL.."

        示例 2：
        输入："RR.L"
        输出："RR.L"
        说明：第一张多米诺骨牌没有给第二张施加额外的力。
        https://leetcode-cn.com/problems/push-dominoes
        '''
        self.dic = {}

    def pushDominoes1(self, dominoes: str) -> str:
        if len(dominoes) <= 1:
            return dominoes
        for i, v in enumerate(dominoes):
            if v == '.':
                self.dic[i] = Effect(0, v)
            else:
                self.dic[i] = Effect(1, v)
        move = sum([1 if e.status == 1 else 0 for e in self.dic.values()])
        while move > 0:
            for i in range(len(dominoes)):
                if self.dic[i].status > 0:
                    self.dic[i].status = 2
                    self.dic[i].before = self.dic[i].cur
                    continue
                if i == 0:
                    next = self.dic[i + 1]
                    pre = None
                elif i == len(dominoes) - 1:
                    next = None
                    pre = self.dic[i - 1]
                else:
                    next = self.dic[i + 1]
                    pre = self.dic[i - 1]
                l, r = 0, 0
                if pre and pre.before == 'R':
                    r += 1
                if next and next.cur == 'L':
                    l += 1
                if l == r:
                    # self.dic[i].before = self.dic[i].cur
                    pass
                elif l < r:
                    self.dic[i].status = 1
                    self.dic[i].before = self.dic[i].cur
                    self.dic[i].cur = 'R'
                else:
                    self.dic[i].status = 1
                    self.dic[i].before = self.dic[i].cur
                    self.dic[i].cur = 'L'
            move = sum([1 if s.status == 1 else 0 for s in self.dic.values()])
        return ''.join([e.cur for e in self.dic.values()])

    def pushDominoes2(self, dominoes):
        li = list(dominoes)
        before = ''
        start = -1
        for i, v in enumerate(dominoes):
            cur = v
            if cur != '.':
                if start > -1:
                    if before == cur:
                        li[start:i] = [cur] * (i - start)
                    elif before != 'L':
                        div, mod = divmod(i - start, 2)
                        if start == 0:
                            if cur != 'R':
                                li[start:i] = [cur] * i
                        elif div > 0:
                            if before == 'R':
                                li[start:start + div] = [before] * div
                            if v == 'L':
                                li[start + div + mod:i] = [cur] * div
                    start = -1
                before = v
            else:
                if start == -1:
                    start = i
        if start != -1 and before == 'R':
            li[start:len(dominoes)] = [before] * (len(dominoes) - start)
        return ''.join(li)

    def pushDominoes(self, dominoes: str) -> str:
        pre, res = (-1, 'L'), ''  # 首部的虚拟哨兵
        for i, s in enumerate(dominoes + 'R'):  # 尾部的哨兵
            if s == 'L':
                if pre[1] == 'L':
                    res += 'L' * (i - pre[0])
                else:
                    div, mod = divmod((i - pre[0] - 1), 2)
                    res += 'R' * div + '.' * mod + 'L' * div + 'L'
                pre = (i, s)
            elif s == 'R':
                if pre[1] == 'L':
                    res += '.' * (i - pre[0] - 1) + 'R'
                else:
                    res += 'R' * (i - pre[0])
                pre = (i, s)
        return res[:-1]  # 去掉尾部的哨兵

if __name__ == '__main__':
    s = Solution()
    tmp = "..RL...L.R.R.......LL.....L.L..L.....R...R........LR...L.R....L.R....R.L.R.....RR.........R.......RR.RLL..L..R....L..R..L..R.R...L.....R..........R....RL.............L...R....R...........LR...L...R....R.R....................R...RLR..R......RL........L.....L......R.......R.R...R..........LL....LRL.L...........L......L.....RL.....R...R.....................L...L.R....R...L..R......R..L.....R....................L"
    # tmp = td.s
    # print(tmp)
    print(tmp)
    print(s.pushDominoes(tmp), len(s.pushDominoes(tmp)))
    print(s.pushDominoes2(tmp), len(s.pushDominoes2(tmp)))
    # print("LLLLRR.LLLLL.....RRL...")
