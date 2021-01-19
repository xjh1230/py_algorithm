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
        名称概念：
        LRU (Least recently used) 最近最少使用，如果数据最近被访问过，那么将来被访问的几率也更高。
        LFU (Least frequently used) 最不经常使用，如果一个数据在最近一段时间内使用次数很少，那么在将来一段时间内被使用的可能性也很小。
        FIFO (Fist in first out) 先进先出， 如果一个数据最先进入缓存中，则应该最早淘汰掉。
        设计并实现最不经常使用（LFU）缓存的数据结构。它应该支持以下操作：get 和 put。

        可见LRU关键是看页面最后一次被使用到发生替换的时间长短，时间越长，页面就会被置换； 而LFU关键是看一定时间段内页面被使用的频率（次数），使用频率越低，页面就会被置换。
        也就是说： LRU算法适合：较大的文件比如游戏客户端（最近加载的地图文件） LFU算法适合：较小的文件和教零碎的文件比如系统文件、应用程序文件 其中：LRU消耗CPU资源较少，LFU消耗CPU资源较多。

        get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
        put(key, value) - 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效
        。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，最近最少使用的键将被去除。
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}  # 存放数据 {'key':'value'}
        self.dic_reference = {}  # 存放数据引用次数，时间{'key':{'count':'count','time':'time'}}
        self.dic_count = {}  # 存放某个引用次数的key个数 {1次:10个}

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
                tmp = self.dic_count.get(count, 0)
                if tmp <= 0:
                    count += 1
                else:
                    tmp_time = time.time()
                    tmp_key = -1
                    for tu in self.dic_reference.items():
                        # print(tu, tmp_time)
                        if tu[1].get('count') == count:
                            if tmp == 0:
                                break
                            tmp -= 1
                            if tu[1].get('time') <= tmp_time:
                                tmp_key = tu[0]
                                tmp_time = tu[1].get('time')
                    # print(tmp_key, count, self.dic_count, self.dic_reference)
                    del self.dic_reference[tmp_key]
                    del self.dic[tmp_key]
                    self.dic_count[count] = self.dic_count[count] - 1
                    break

    def _set_count(self, key):
        tmp = self.dic_reference.get(key, {})
        count = tmp.get('count', 0) + 1
        tmp['count'] = count
        tmp['time'] = time.time()
        self.dic_reference[key] = tmp

        tmp = self.dic_count.get(count, 0)
        self.dic_count[count] = tmp + 1

        tmp = self.dic_count.get(count - 1, -1)
        if tmp <= 0:
            tmp = 1
        self.dic_count[count - 1] = tmp - 1


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
