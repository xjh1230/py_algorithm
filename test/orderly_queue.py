# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 15:01
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : orderly_queue.py
# @Software: PyCharm

class Solution:
    def orderlyQueue(self, S, K):
        """
        给出了一个由小写字母组成的字符串 S。然后，我们可以进行任意次数的移动。

在每次移动中，我们选择前 K 个字母中的一个（从左侧开始），将其从原位置移除，并放置在字符串的末尾。

返回我们在任意次数的移动之后可以拥有的按字典顺序排列的最小字符串。
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S
        k = K
        if len(s) <= 1:
            return s
        ii = 0
        while not self.check_sort(s, k) and ii < 20:
            ii += 1
            index = 0
            if k > 1:
                for i in range(1, k + 1):
                    if i >= len(s):
                        break
                    # 没有排序，取最小的放最后
                    if not self.sorted(s[k:]):
                        if s[i - 1] < s[i]:
                            index = i - 1
                            break
                        else:
                            i += 1
                    # 已经排序，放小的到后面
                    else:
                        if s[i - 1] > s[i]:
                            index = i - 1
                            break
                        else:
                            i += 1

                    index = k - 1
                if index == 0:
                    s = s[1:] + s[index]
                    print(index, s, 'index==0', k)
                else:
                    s = s[:index] + s[index + 1:] + s[index]
                    print(index, s, 'index>0', k)
        return s

    def check_sort(self, s, k, next_flag=False):
        '''
        :param s:
        :param k:
        :return:
        '''
        max_c = ''
        if not next_flag:
            # 前k位已经排序
            for i in range(1, k):
                if s[i - 1] > s[i]:
                    return False
            # 前k位的最大值
            for i in range(len(s[:k])):
                if max_c < s[i]:
                    max_c = s[i]
                i += 1
            # 后面有比前k位最大值小的
            for i in s[k:]:
                if i < max_c:
                    return False
        compared = s[:k]
        for i in range(1, len(s)):
            tmp = s[i:i + k]
            if len(tmp) < k:
                return compared[:len(tmp) - 1] <= tmp
            else:
                if compared > tmp:
                    return False
                else:
                    if compared == tmp:
                        return self.check_sort(s, k + 1, True)
                    i += 1
        return True

    def sorted(self, s):
        for i in range(1, len(s)):
            if s[i - 1] > s[i]:
                return False
        return True

    def test(self):
        s = '42351'
        k = 2
        print(self.orderlyQueue(s, k), s, k)
        # print(self.orderlyQueue('baaca', 3), 'baaca', 3)
        # print(self.orderlyQueue('gxzv', 3), 'gxzv', 3)


if __name__ == '__main__':
    s = Solution()
    s.test()
