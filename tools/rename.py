# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 10:55
# @Author  : Xingjh
# @Email   : xjh_0125@sina.com
# @File    : rename.py
# @Software: PyCharm

import os, shutil


def get_all_path():
    path = 'D:\BaiduNetdiskDownload\笔记+源代码(1)\笔记+源代码\CSS&CSS3资料\CSS3入门及提高资料\CSS3入门及提高资料'
    path_dir = os.listdir(path)
    for p in path_dir:
        if p.startswith('.'):
            continue
        child = os.path.join('%s\%s\%s' % (path, p, '案例'))
        for root, dirs, files in os.walk(child):
            for file in files:
                if file.endswith('.html'):
                    file_new = file.replace(' ', '')
                    if file != file_new:
                        shutil.move(os.path.join(child, file), os.path.join(child, file_new))


# get_all_path()
p = 'D:\BaiduNetdiskDownload\笔记+源代码(1)\笔记+源代码\CSS&CSS3资料\CSS3入门及提高资料\CSS3入门及提高资料\CSS3入门及提高01和02\案例'


# for root, dirs, files in os.walk(p):
#     print(root)
#     print(dirs)
#     print(files)
#     shutil.move(os.path.join(root, files[0]), os.path.join(root, '1.html'))
#     break


def rename_img():
    path = 'img2'
    path_dir = os.listdir(path)
    i = 1
    for p in path_dir:
        shutil.move(os.path.join(path, p), os.path.join('img2', str(i) + '.png'))
        i += 1


rename_img()
