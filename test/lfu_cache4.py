# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 16:42
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : lfu_cache.py
# @Software: PyCharm

import time


class Node:
    def __init__(self, key, val, count, front_node=None, next_node=None):
        self.key = key
        self.val = val
        self.count = count
        self.front_node = front_node
        self.next_node = next_node


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
        self.lase_node = None
        self.dic = {}
        self.dic_count = {}
        self.max_count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity <= 0:
            return -1
        node = self.dic.get(key, None)
        if node:
            self._set_count(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if self.dic.__contains__(key):  # 直接更新
            self.dic[key].val = value
        else:
            if len(self.dic) >= self.capacity:  # 删除最后一个
                self._remove_expire()
            node = Node(key, value, 0)
            self.dic[key] = node
        self._set_count(self.dic[key])

    def _remove_expire(self):
        if len(self.dic) >= self.capacity:  # 找到需要删除的值，
            # print('超出范围')
            try:
                tmp = self.lase_node
                if tmp:
                    # if self.dic.__contains__(tmp.key):
                    del self.dic[tmp.key]
                    self.lase_node = tmp.front_node
            except:
                pass

    def _set_count(self, node):
        if not self.lase_node:
            self.lase_node = node
        elif self.lase_node.key == node.key:
            if node.next_node:
                self.lase_node = node.next_node
            elif node.front_node:
                self.lase_node = node.next_node
        elif self.lase_node.count > node.count + 1:
            self.lase_node = node
        count = node.count
        # 当前节点从链表中移除
        if node.front_node:
            node.front_node.next_node = node.next_node
            # node.next_node = None
        if node.next_node:
            node.next_node.front_node = node.front_node
            # node.front_node = None

        # 将当前节点放入对应位置
        tmp_node = self.dic_count.get(count, None)
        if tmp_node and tmp_node.key == node.key:
            tmp_node = node.next_node
            self.dic_count[count] = tmp_node

        count += 1
        node.count = count
        self.max_count = count if count > self.max_count else self.max_count
        node.front_node = None
        while count <= self.max_count:
            if count == node.count:
                tmp_node = self.dic_count.get(count, None)
                if tmp_node and tmp_node.key:
                    if tmp_node.front_node:
                        tmp_node.front_node.next_node = node
                    node.front_node = tmp_node.front_node
                    node.next_node = tmp_node
                    tmp_node.front_node = node
                    # print(node.key, '+++++', tmp_node.key)
                    self.dic_count[count] = node
                    break
                else:
                    self.dic_count[count] = node
                    tmp_count = count - 1
                    while tmp_count > 0:
                        tmp_node = self.dic_count.get(tmp_count, None)
                        if tmp_node:
                            node.next_node = tmp_node
                            tmp_node.front_node = node
                            break
                        tmp_count -= 1

            else:
                tmp_node = self.dic_count.get(count, None)
                if tmp_node:
                    while True:
                        if not tmp_node.next_node or tmp_node.next_node.count != count:
                            break
                        tmp_node = tmp_node.next_node
                    node.next_node = tmp_node.next_node
                    node.front_node = tmp_node
                    tmp_node.next_node = node
                    if tmp_node.next_node:
                        tmp_node.next_node.front_node = node
                    break
                    # print(node.key, '------', tmp_node.key)
            count += 1


# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
# [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
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
        if len(li[i]) == 1:
            # print(li[i])
            print(obj.get(li[i][0]))
        else:
            # print(li[i])
            obj.put(li[i][0], li[i][1])
