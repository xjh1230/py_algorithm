# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 14:31
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : down_audio.py
# @Software: PyCharm

import os
import requests


class DownLoad:
    def __init__(self):
        self.video_path = os.path.join('D:\data\ekwing', 'video')
        self.audio_path = os.path.join('D:\data\ekwing', 'audio')
        self.img_path = os.path.join('D:\data\ekwing', 'img')
        self.confirm_path(self.video_path)
        self.confirm_path(self.audio_path)

    def down(self, video):
        video_path = video.audio
        video_audio = video.video_audio
        video_img = video.video_img
        if video_path != '':
            if self._get(video_path, self.video_path):
                video.update_video()
        if video_audio != '':
            if self._get(video_audio, self.audio_path):
                video.update_audio()
        if video_img != '':
            if self._get(video_img, self.img_path):
                video.save_img()

    def _get(self, url, save_path):
        try:
            name = url.split('/')[-1]
            res = requests.get(url, verify=False)
            res.raise_for_status()
            file = open(os.path.join(save_path, name), 'wb')
            for chunk in res.iter_content(100000):
                file.write(chunk)
            return True
        except BaseException as e:
            return False

    def confirm_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)



if __name__ == '__main__':
    d = DownLoad()
    url = 'https://cdn-ekwing-oss-new.ekwing.com/acpf/data/upload/expand/2017/08/22/599bce17ba604.mp4'
    d.down(url)
