# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 14:42
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : judge_point_24.py
# @Software: PyCharm

class Solution:
    def judgePoint24_1(self, nums):
        bad = '对撒剘劥圞剜劏哱掶桺泛揋掵従剟剣彫寣污悫壛梄甏咍哲汭剤堧点卋嬞勆叛汬泐塵栋劚嚮咃宠吖剗楗囧力桻攋壯劯嗏桹劙剢剚焧啫栕炸栫栖嚲彳剛撑烃洿宋汷彲剙揁妷埻撧汢吩壙劇剭埼吕剝汣敯憇勇剥咎囻匓'
        return chr(int(''.join(map(str, sorted(nums)))) + 19968) not in bad

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != 4:
            raise ValueError
        li = self.get_result_13(nums)
        li.extend(self.get_result_22(nums))
        eps = 0.0001
        for i in li:
            if i == 24 or abs(24 - i) < eps:
                print(i)
                return True
        return False

    def get_result_13(self, nums):
        li = []
        count = len(nums)
        if count < 2:
            raise ValueError
        elif count == 2:
            return self.calc_num(nums[0], nums[1])
        else:
            for i in range(len(nums)):
                li_tmp = self.get_result_13(nums[0:i] + nums[i + 1:])
                for j in li_tmp:
                    li.extend(self.calc_num(nums[i], j))
        return li

    def get_result_22(self, nums):
        li = []
        # li.extend(self.calc_num(nums[0],nums[1]))
        for i in range(1, len(nums) - 1):
            tmp_1 = self.calc_num(nums[0], nums[i])

            tmp = 6 - i
            be_sub = 3 if 3 < tmp else tmp - 1
            index_1 = tmp - be_sub
            index_2 = tmp - index_1
            tmp_2 = self.calc_num(nums[index_1], nums[index_2])
            li.extend(self.calc_nums(tmp_1, tmp_2))
        return li

    def calc_nums(self, nums1, nums2):
        li = []
        for i in nums1:
            for j in nums2:
                li.extend(self.calc_num(i, j))
        return li

    def calc_num(self, num1, num2):
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 == 0:
            return []
        elif num1 == 0:
            return [num2, -num2]
        else:
            return [num1 + num2, num1 - num2, num2 - num1, num1 * num2, num1 / num2, num2 / num1]


import itertools


class Solution1:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        eps = 0.0001

        def reduce(arr):
            '''
            :param arr: set
            :return:
            '''
            if len(arr) == 1:
                return abs(arr[0] - 24) < eps
            for i in range(len(arr) - 1):
                a, b = arr[i], arr[i + 1]
                rs = [a + b, a - b, a * b] + [a / b] if abs(b) > eps else []
                if any((reduce(arr[:i] + (r,) + arr[i + 2:])) for r in rs):
                    return True
            return False

        return any((reduce(arr) for arr in set(itertools.permutations(nums))))


if __name__ == '__main__':
    c = Solution()
    print(c.judgePoint24([3, 3, 8, 8]))  # 8/(3-8/3)
    print(c.judgePoint24([1, 3, 4, 6]))  # (4/1)*(6-3)
    print(c.judgePoint24([1, 9, 1, 2]))  # (4/1)*(6-3)
