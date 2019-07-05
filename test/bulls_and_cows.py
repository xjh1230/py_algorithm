# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 11:03
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : bulls_and_cows.py
# @Software: PyCharm
import collections
import operator


class Solution:
    def __init__(self):
        '''
        https://leetcode-cn.com/problems/bulls-and-cows/
        你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。

请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

请注意秘密数字和朋友的猜测数都可能含有重复数字。

示例 1:

输入: secret = "1807", guess = "7810"

输出: "1A3B"

解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
示例 2:

输入: secret = "1123", guess = "0111"

输出: "1A1B"

解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bulls-and-cows
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        '''
        pass

    def getHint1(self, secret: str, guess: str) -> str:
        bulls = [i for i in range(len(secret)) if secret[i] == guess[i]]
        bulls = sum(map(operator.eq, guess, secret))
        count = 0
        secret = [s for s in secret]
        for g in guess:
            if g in secret:
                count += 1
                secret.pop(secret.index(g))
        res = str(len(bulls)) + 'A' + str(count - len(bulls)) + 'B'
        return res

    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, (both - bulls))


if __name__ == '__main__':
    s = Solution()
    res = s.getHint('1123', '0111')
    # collections.Counter('111')
    print(res)
