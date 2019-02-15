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
    obj = LFUCache(2)
    print(obj.get(1))
    obj.put(1, 2)
    print(obj.get(2))
    obj.put(2, 2)
    obj.put(3, 2)
    print(obj.get(2))
    print(obj.get(1))
    print(obj.dic_count, obj.dic_reference, obj.dic)
