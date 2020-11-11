#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        def gen(i):
            c = len(res)
            for arr in range(c):
                tmp = [j for j in res[arr]]
                tmp.append(nums[i])
                res.append(tmp)

        res = [[]]
        for i in range(len(nums)):
            gen(i)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))

# @lc code=end
