# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 11:20
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : tanxin_suanfa.py
# @Software: PyCharm

def moveCard():
    heap = 3
    cards = [1, 2, 27]
    count, needs = move(cards, heap)
    print(count, needs)
    for i in range(len(cards)):
        print('第%d堆牌数：%d' % (i + 1, cards[i]))


def move(cards, heap):
    avg = sum(cards) // heap
    needs = []
    count = 0
    for i in range(len(cards)):
        need = avg - cards[i]
        cards[i] += need
        if i < len(cards) - 1:
            cards[i + 1] -= need
            needs.append(need)
        if need != 0:
            count += 1

    return (count, needs)


if __name__ == '__main__':
    moveCard()
