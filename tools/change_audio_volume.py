#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : 1230
# @Email   : xjh_0125@sina.com
# @Time    : 2019/11/20 18:53
# @Software: PyCharm
# @File    : cut_audio.py

from pydub import AudioSegment
from pydub.silence import detect_silence
import os

q = 500


class change_audio_vokumn:
    def __init__(self):
        """
        """
        pass

    def cut_file(self):
        path_dir = os.listdir('mp3')
        for file in path_dir:
            file = file.lower()
            if file.endswith('.mp3'):
                file = 'mp3/' + file
                self.cut(file)

    def cut(self, file_name):
        sound = AudioSegment.from_mp3(file_name)
        start_end = detect_silence(sound, 300, -35, 1)
        print(start_end)
        # start = '0:05'
        # end = '0:20'
        # start_time = (int(start.split(':')[0]) * 60 + int(start.split(':')[1])) * 1000
        # stop_time = (int(end.split(':')[0]) * 60 + int(end.split(':')[1])) * 1000
        stop_time = len(sound)
        start_time = start_end[0][1]
        if start_time > q:
            start_time -= q
        word = sound[start_time:stop_time]
        save_name = file_name[0:len(file_name) - 4] + '1.mp3'
        word.export(save_name, format="mp3", tags={'artist': 'AppLeU0', 'album': save_name[:-4]})


if __name__ == '__main__':
    s = cut_audio()
    s.cut_file()
