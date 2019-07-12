# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 17:41
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : lexicographical_numbers.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        '''
        给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lexicographical-numbers
        '''

    def lexicalOrder(self, n: int):
        def can_push(cur):
            return n >= cur * 10

        def can_add(cur):
            return n >= cur

        def generate_one(cur):
            stack, result = [cur], []
            if can_add(cur):
                result.append(cur)
            else:
                return []
            while can_push(cur):  # 依此将 *x0 插入
                cur = cur * 10
                result.append(cur)
                stack.append(cur)
            while len(stack) > 1:
                cur = stack.pop(-1) + 1
                if can_push(cur):  # 依此将 （*+1)x0插入
                    for j in range(9):
                        result.extend(generate_one(cur))
                        cur += 1
                elif can_add(cur):
                    result.append(cur)
                    for i in range(8):
                        if can_add(cur + 1):
                            cur = cur + 1
                            result.append(cur)
                        else:
                            break

            return result

        if n < 1:
            return []
        else:
            res = []
            for i in range(1, 10):
                res.extend(generate_one(i))
            return res


if __name__ == '__main__':
    s = Solution()
    li = s.lexicalOrder(2000)
    print(li)
    print(len(li))
