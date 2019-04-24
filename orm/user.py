#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/4/20 12:07
# software: PyCharm

# from sqlsever_orm import Model, IntegerField, StringField
import sqlsever_orm
import mysql_orm
from config import configs
import asyncio


class User(mysql_orm.Model):
    __table__ = 'user'
    id = mysql_orm.IntegerField('id', primary_key=True)
    name = mysql_orm.StringField('name')


class User2(sqlsever_orm.Model):
    __table__ = 'user'
    id = sqlsever_orm.IntegerField('id', primary_key=True)
    name = sqlsever_orm.StringField('name')


@asyncio.coroutine
def test(loop):
    yield from mysql_orm.create_pool(loop, **configs.db)
    u = User(id=3, name='1111')
    yield from u.update()
    users = yield from u.findAll()
    for i in users:
        print(i)


def test2():
    sqlsever_orm.create_pool(**configs.db)
    u = User2(id=5, name='3333')
    print(u)
    u.name = '2333'
    print(u)
    # u.update()
    # users = u.findAll()
    # for i in users:
    #     print(i)


if __name__ == '__main__':
    # 获取EventLoop:
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test(loop))
    # loop.stop()
    test2()
