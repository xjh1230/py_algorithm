# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 16:11
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : skip_list.py
# @Software: PyCharm

import random


class CNode:
    def __init__(self, level=0, key=None, value=None):
        self.key = key
        self.value = value
        self.next = [None] * level  # level层


class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.headers = CNode(max_level)
        self.size = 0
        self.level = 0
        self.delete_count = 0

    def insert(self, key, value):
        node = self.get(key)
        if node:
            node.value = value
            return True
        else:
            self.size += 1
            level = self.random_level()
            node = CNode(level, key, value)
            self.level = level if level > self.level else self.level
            i = 0
            while i < level:
                tmp = self.headers.next[i]
                while tmp and tmp.next[i] and tmp.next[i].key <= key:
                    tmp = tmp.next[i]
                if tmp:
                    node.next[i] = tmp.next[i]
                    tmp.next[i] = node
                else:
                    self.headers.next[i] = node
                i += 1
            return True

    def get(self, key):
        i = self.level - 1
        while i >= 0:
            tmp = self.headers
            while tmp.next[i] and (tmp.next[i].key <= key or tmp.next[i].key == -1):
                if tmp.next[i].key == key:
                    return tmp.next[i]
                elif tmp.next[i].key == -1:
                    tmp_next = tmp.next[i]
                    while tmp_next and tmp_next.key == -1:
                        tmp_next = tmp_next.next[i]
                    if not tmp_next or tmp_next.key > key:
                        break
                    elif tmp_next.key == key:
                        return tmp_next
                    else:
                        tmp = tmp_next
                else:
                    tmp = tmp.next[i]
            i -= 1
        return None

    def random_level(self):
        level = 1
        while random.randint(0, 1) == 1 and level < self.max_level:
            level += 1
        return level

    def delete(self, key):
        node = self.get(key)
        if node:
            node.key = -1
            self.delete_count += 1
            self.size -= 1
            if self.size / self.delete_count <= 2:
                self.clear_delete()
        else:
            return False

    def clear_delete(self):
        i = self.level - 1
        while i >= 0:
            tmp = self.headers.next[i]
            while tmp:
                if tmp.next[i] and tmp.next[i].key == -1:
                    tmp.next[i] = tmp.next[i].next[i]
                else:
                    tmp = tmp.next[i]
            i -= 1
        self.delete_count = 0


if __name__ == '__main__':
    s = SkipList(5)
    for i in range(10):
        s.insert(i, i)

    for i in range(10):
        if i % 2 == 0:
            s.delete(i)
            tmp = s.headers.next[0]
            while tmp:
                print(tmp.key, s.delete_count, s.size)
                tmp = tmp.next[0]
            print('-------------')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    s.delete(9)
    for i in range(10):
        tmp = s.get(i)
        if tmp:
            print(tmp.key)
    print(s.delete_count, s.size)
