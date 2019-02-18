# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 16:42
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : lfu_cache.py
# @Software: PyCharm

import time


class LFUCache:
    def __init__(self, capacity):
        """
        设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效
。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}  # 存放数据 {'key':'value'}
        self.dic_reference = {}  # 存放数据引用次数 {'key':'count'}
        self.dic_count = {}  # 从放当前引用次数下所有key，及时间 {1:{'key':'time'}}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity <= 0:
            return -1
        result = self.dic.get(key, -1)
        if result != -1:
            self._set_count(key)
        return result

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if self.dic.__contains__(key) or len(self.dic) < self.capacity:  # 直接更新新值
            self._set_count(key)
            self.dic[key] = value
        else:
            self._remove_expire()
            self._set_count(key)
            self.dic[key] = value

    def _remove_expire(self):
        if len(self.dic) >= self.capacity:  # 找到需要删除的值，
            # print('超出范围')
            removed = False
            count = 1
            # print(obj.dic_count, obj.dic_reference, obj.dic)
            while not removed:
                tmp = self.dic_count.get(count, {})
                if len(tmp) == 0:
                    count += 1
                else:
                    tmp_time = time.time()
                    tmp_key = -1
                    for tu in self.dic_count[count].items():
                        # print(tu, tmp_time)
                        if tu[1] <= tmp_time:
                            tmp_key = tu[0]
                            tmp_time = tu[1]
                    # print(tmp_key, count, self.dic_count, self.dic_reference)
                    del self.dic_reference[tmp_key]
                    del self.dic[tmp_key]
                    del self.dic_count[count][tmp_key]
                    break

    def _set_count(self, key):
        tmp = self.dic_reference.get(key, 0)
        count = tmp + 1
        self.dic_reference[key] = count
        # 前一个使用次数删除该key
        if count > 1:
            del self.dic_count[count - 1][key]
        # 后一个使用次数添加该key
        tmp = self.dic_count.get(count, 0)
        if tmp == 0:
            self.dic_count[count] = {key: time.time()}
        else:
            self.dic_count[count][key] = time.time()


if __name__ == '__main__':
    li = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
          [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
          [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
          [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
          [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
          [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27],
          [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
          [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    obj = LFUCache(li[0][0])
    # print(obj.get(1))
    # obj.put(1, 2)
    # print(obj.get(2))
    # obj.put(2, 2)
    # obj.put(3, 2)
    # print(obj.get(2))
    # print(obj.get(1))
    # print(obj.dic_count, obj.dic, obj.max_count, obj.lase_node)

    for i in range(1, len(li)):
        if i == 58:
            tt = i
        if len(li[i]) == 1:
            print('get', obj.get(li[i][0]), i, li[i], len(obj.dic))
        else:
            # print('put:start', i, li[i], len(obj.dic))
            obj.put(li[i][0], li[i][1])
            # print('put:end', i, li[i], len(obj.dic))  # , obj.lase_node.key)
