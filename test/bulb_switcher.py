# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 14:19
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : bulb_switcher.py
# @Software: PyCharm

import math


class Solution:
    def __init__(self):
        '''
            https://leetcode-cn.com/problems/bulb-switcher/submissions/
            初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例:

输入: 3
输出: 1
解释:
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭].

你应该返回 1，因为只有一个灯泡还亮着。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bulb-switcher
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        '''
        pass

    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)

    def bulbSwitch1(self, n: int) -> int:
        def calc(num):
            a = int((math.sqrt(num)))
            return a * a == num

        li = [1 for i in range(1, n + 1) if calc(i)]
        return sum(li)


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.bulbSwitch(i))
