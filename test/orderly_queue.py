# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 15:01
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : orderly_queue.py
# @Software: PyCharm

class Solution:
    def orderlyQueue(self, S, K):
        """
        没成功
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
        max_value = s[0]
        min_value = s[0]
        for i in s:
            if i > max_value:
                max_value = i
            if i < min_value:
                min_value = i

        while not self.check_sort(s, k):  # and ii < 20:
            index = 0
            hax_max = False
            has_min = False
            all_equal = False
            if k >= len(s):
                for i in range(0, len(s) - ii):
                    if s[i] < s[index]:
                        index = i
            elif k > 1:
                index = -1
                last = s[-1]
                has_max = False
                has_equal = False
                max_index = -1
                min_index = -1
                for i in range(k):
                    if s[i] == max_value:
                        max_index = max_index if min_index != -1 else i
                    if s[i] == min_value:
                        min_index = min_index if min_index != -1 else i
                if min_index != -1 and max_index != -1 and 1 == 2:
                    index = min_index
                else:
                    for i in range(k):
                        if s[i] == last and not self.all_equal(s[i:k + 1]):
                            index = i
                            has_equal = True
                            break
                        elif s[i] > last:
                            if index == -1:
                                index = i
                            else:
                                index = i if s[i] < s[index] else index
                            hax_max = True
                    if not hax_max and not has_equal:
                        index = 0
                        for i in range(k):
                            if s[i] < s[index]:
                                index = i
            if index <= 0:
                index = 0
                s = s[1:] + s[index]
                # print('haxMax', hax_max, index, s, 'index==0', k)
            else:
                s = s[:index] + s[index + 1:] + s[index]
                # print('haxMax', hax_max, index, s, 'index>0', k)
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
            if k == len(s):
                return True
            # 前k位的最大值
            for i in range(len(s[:k])):
                if max_c < s[i]:
                    max_c = s[i]
                i += 1
            # 后面有比前k位最大值小的
            for i in s[k:]:
                if i < max_c:
                    return False

        if k > 1:
            tmp = self.sorted(s[k:])
            return tmp
        else:
            k = k + 1
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

    def all_equal(self, s):
        tmp = s[0]
        for i in s:
            if i != tmp:
                return False
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
        # print(self.orderlyQueue(s, k), s, k)
        # print(self.orderlyQueue('321', 1), '321', 1)
        # print(self.orderlyQueue('13112', 1), '13112', 1)
        # print(self.orderlyQueue('13112', 2), '13112', 2)
        # print(self.orderlyQueue('13112', 3), '13112', 3)
        # print(self.orderlyQueue('13112', 4), '13112', 4)
        # print(self.orderlyQueue('13112', 5), '13112', 5)
        # print(self.orderlyQueue('3231', 1), '3231', 1)
        # print(self.orderlyQueue('3231', 2), '3231', 2)
        # print(self.orderlyQueue('3231', 3), '3231', 3)
        # print(self.orderlyQueue('3231', 4), '3231', 4)
        # print(self.orderlyQueue('33132', 1), '33132', 1)
        # print(self.orderlyQueue('33132', 2), '33132', 2)
        # print(self.orderlyQueue('33132', 3), '33132', 3)
        # print(self.orderlyQueue('33132', 4), '33132', 4)
        # print(self.orderlyQueue('33132', 5), '33132', 5)
        # print(self.orderlyQueue('234215', 1), '234215', 1)
        # print(self.orderlyQueue('234215', 1), '234215', 1)
        # print(self.orderlyQueue('234125', 2), '234215', 2)
        # print(self.orderlyQueue('234215', 3), '234215', 3)
        # print(self.orderlyQueue('234215', 4), '234215', 4)
        # print(self.orderlyQueue('234215', 5), '234215', 5)
        # print(self.orderlyQueue('234215', 6), '234215', 6)
        # print(self.orderlyQueue("qwzwkluwnqwroyyxtsrsxqnpusqzkoaabbbccdddefhhhhiijj", 50),
        #       "qwzwkluwnqwroyyxtsrsxqnpusqzkoaabbbccdddefhhhhiijj", 50)
        # print(self.orderlyQueue('78562431', 2), '78562431', 2)
        print(self.orderlyQueue('226224223', 1), '78562431', 2)


if __name__ == '__main__':
    s = Solution()
    s.test()
    # print(s.check_sort('123345', 6))
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
