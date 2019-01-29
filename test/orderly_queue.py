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
        k = K if K <= len(S) else len(S)
        if len(s) <= 1 or k < 1:
            return s
        ii = 0
        while not self.check_sort(s, k) and ii < 20:
            index = 0
            has_sort = True
            hax_max = False
            has_min = False
            all_equal = False
            has_equal = False
            if k >= len(s):
                for i in range(0, len(s) - ii):
                    if s[i] <= s[index]:
                        index = i
            elif k > 1:
                # 如果前面全都相同或者全大于后面，统一全部后移
                all_equal = True
                for i in range(k):
                    if s[i] != s[0]:
                        all_equal = False
                        break
                all_greate = True
                for i in s[k:]:
                    if s[index] <= i:
                        all_greate = False
                        break
                if all_equal or all_greate:
                    # print('all_equal前', i, s)
                    s = s[k:] + s[:k]
                    # print('all_equal后', s)
                    continue
                # 已经排序，取大于等于最后一个的最小值，或者最小值
                has_sort = self.sorted(s[k:])
                # print(has_sort, s[k:])
                if has_sort:
                    # 是否有大于最大值的值
                    all_equal = (s[k] == s[-1])  # 如果最后的值n全相等，则如果前面有比他n还小的就移动n，没有就不移动n
                    if all_equal:
                        for i in range(k):
                            if s[i] > s[-1]:
                                hax_max = True
                            elif s[i] < s[-1]:
                                has_min = True
                            else:
                                has_equal = True
                        # 有大于等于最后一个的 取大于等于的最小值
                        # 如果最后的值n全相等，则如果前面有比他n还小的就移动n，没有就不移动n
                        if hax_max:
                            for i in range(k):
                                if s[i] > s[-1]:
                                    # if not all_equal:
                                    index = i if s[i] < s[index] else index

                        elif has_min:
                            for i in range(k):
                                if s[i] < s[index]:
                                    index = i
                        else:
                            for i in range(k):
                                if s[i] == s[-1]:
                                    index = i
                                    break
                    else:
                        index = -1
                        for i in range(k):
                            if s[i] > s[-1]:
                                index = index if index != -1 and s[i] > s[index] else i
                # 没有排序，取最小的放最后
                else:
                    for i in range(k):
                        if s[i] < s[index]:
                            index = i

            if index <= 0:
                index = 0
                s = s[1:] + s[index]
                # print('haxMax', hax_max, 'has_sort', has_sort, index, s, 'index==0', k)
            else:
                s = s[:index] + s[index + 1:] + s[index]
                # print('haxMax', hax_max, 'has_sort', has_sort, index, s, 'index>0', k)
            ii += 1
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
        if len(s) == 0:
            return False
        for i in range(1, len(s)):
            if s[i - 1] > s[i]:
                return False
        return True

    def test(self):
        #   461257
        s = '456712'
        k = 2
        print(self.orderlyQueue(s, k), s, k)
        print(self.orderlyQueue('321', 1), '321', 1)
        print(self.orderlyQueue('13112', 1), '13112', 1)
        print(self.orderlyQueue('13112', 2), '13112', 2)
        print(self.orderlyQueue('13112', 3), '13112', 3)
        print(self.orderlyQueue('13112', 4), '13112', 4)
        print(self.orderlyQueue('13112', 5), '13112', 5)
        print(self.orderlyQueue('3231', 1), '3231', 1)
        print(self.orderlyQueue('3231', 2), '3231', 2)
        print(self.orderlyQueue('3231', 3), '3231', 3)
        print(self.orderlyQueue('3231', 4), '3231', 4)
        print(self.orderlyQueue('33132', 1), '33132', 1)
        print(self.orderlyQueue('33132', 2), '33132', 2)
        print(self.orderlyQueue('33132', 3), '33132', 3)
        print(self.orderlyQueue('33132', 4), '33132', 4)
        print(self.orderlyQueue('33132', 5), '33132', 5)
        print(self.orderlyQueue('234215', 1), '234215', 1)
        print(self.orderlyQueue('234215', 1), '234215', 1)
        print(self.orderlyQueue('234215', 2), '234215', 2)
        print(self.orderlyQueue('234215', 3), '234215', 3)
        print(self.orderlyQueue('234215', 4), '234215', 4)
        print(self.orderlyQueue('234215', 5), '234215', 5)
        print(self.orderlyQueue('234215', 6), '234215', 6)


if __name__ == '__main__':
    s = Solution()
    s.test()
    # s = '11112'
    # k = 3
    # s1 = s[:k]
    # s2 = s[k:]
    # index = -1
    # for i in range(1, k):
    #     if i >= len(s):
    #         break
    #     if s[i - 1] >= s[-1] and s[i - 1] > s[k]:
    #         if index > -1:
    #             index = index if s[i - 1] > s[index] else i - 1
    #         else:
    #             index = i - 1
    #
    # print(index)
