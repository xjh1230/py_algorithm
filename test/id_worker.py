# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 9:50
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : id_worker.py
# @Software: PyCharm


import time


class IdWorker:
    def __init__(self, work_id, data_center_id, sequence):
        '''
        snowflake 实现全局唯一ID
        1bit( 0 无意义，表示正数)|41bit(当前时间戳，到毫秒)|5bit(当前机房Id)|5bit(当前机器Id)|12bit(当前机房当前机器当前毫秒内生成的Id)
        总共64bit
        '''
        self.work_id_bits = 5
        self.data_center_id_bits = 5
        self.sequence_bits = 12
        self.max_work_id = -1 ^ (-1 << self.work_id_bits)
        self.max_data_center_id = -1 ^ (-1 << self.data_center_id_bits)
        self.max_sequence = -1 ^ (-1 << self.sequence_bits)

        self.work_id_left_shift = self.sequence_bits
        self.data_center_id_left_shift = self.sequence_bits + self.work_id_bits
        self.time_stamp_left_shift = self.sequence_bits + self.work_id_bits + self.data_center_id_bits

        if work_id > self.max_work_id or work_id < 0:
            raise ValueError('无效的work_id:%s' % str(work_id))
        if data_center_id > self.max_data_center_id or data_center_id < 0:
            raise ValueError('无效的data_center_id:%s' % str(data_center_id))
        if sequence >= self.max_sequence or sequence < 0:
            raise ValueError('无效的sequence:%s' % str(sequence))
        self.work_id = work_id
        self.data_center_id = data_center_id
        self.sequence = sequence
        self.sequence_mask = -1 ^ (-1 << self.sequence_bits)

        self.last_time_stamp = 0

    def next_id(self):
        time_stamp = self.time_gen()
        if time_stamp < self.last_time_stamp:
            raise Exception('Clock moved backwards. Refusing to generate id for %d milliseconds' % self.last_time_stamp)
        if time_stamp == self.last_time_stamp:
            #  这个意思是说一个毫秒内最多只能有4096个数字，无论你传递多少进来，
            #  这个位运算保证始终就是在4096这个范围内，避免你自己传递个sequence超过了4096这个范围
            # self.sequence_mask = 4095  4095&4096 = 0
            self.sequence = (self.sequence + 1) & self.sequence_mask
            if self.sequence == 0:
                time_stamp = self.get_next_mills()
            self.last_time_stamp = time_stamp
        else:
            self.sequence = 0
            self.last_time_stamp = time_stamp

        result = (self.last_time_stamp << self.time_stamp_left_shift) \
                 | (self.data_center_id << self.data_center_id_left_shift) \
                 | (self.work_id << self.work_id_left_shift) \
                 | self.sequence
        return result

    def time_gen(self):
        return int(time.time() * 1000)

    def get_next_mills(self):
        time_stamp = self.time_gen()
        while time_stamp < self.last_time_stamp:
            time_stamp = self.time_gen()
        return time_stamp

    def test(self):
        for i in range(100):
            tmp = self.next_id()
            bin_tmp = bin(tmp)
            print('%d----%s-----%d' % (tmp, bin_tmp, len(bin_tmp)))


if __name__ == '__main__':
    c = IdWorker(2, 3, 0)
    c.test()
