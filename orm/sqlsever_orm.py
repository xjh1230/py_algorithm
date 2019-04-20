#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/4/20 22:07
# software: PyCharm


import asyncio, logging
import pymysql
from queue import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/tmp/test.log',
                    filemode='w')


def log(sql, args=()):
    logging.error('SQL: %s' % sql)


def create_pool(**kw):
    logging.info('create database connection pool...')
    global __pool
    maxconn = 10
    __pool = Queue(maxconn)
    for i in range(maxconn):
        try:
            conn = pymysql.connect(host=kw.get('host', 'localhost'),
                                   port=kw.get('port', 3306),
                                   user=kw['user'],
                                   password=kw['password'],
                                   db=kw['db'],
                                   charset=kw.get('charset', 'utf8'),
                                   # autocommit=kw.get('autocommit', True),
                                   # maxsize=kw.get('maxsize', 10),
                                   # minsize=kw.get('minsize', 1),
                                   # loop=loop
                                   )
            conn.autocommit(kw.get('autocommit', True))
            __pool.put(conn)
        except Exception  as e:
            raise IOError(e)
        # __pool = pymysql.create_pool(
        #     host=kw.get('host', 'localhost'),
        #     port=kw.get('port', 3306),
        #     user=kw['user'],
        #     password=kw['password'],
        #     db=kw['db'],
        #     charset=kw.get('charset', 'utf8'),
        #     autocommit=kw.get('autocommit', True),
        #     maxsize=kw.get('maxsize', 10),
        #     minsize=kw.get('minsize', 1),
        #     loop=loop
        # )


def select(sql, args, size=None):
    log(sql, args)
    global __pool
    conn = __pool.get()
    try:
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cur:
            cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = cur.fetchmany(size)
            else:
                rs = cur.fetchall()
    except Exception as e:
        __pool.put(conn)
        raise
    else:
        __pool.put(conn)

    logging.info('rows returned: %s' % len(rs))
    return rs


def execute(sql, args, autocommit=True):
    log(sql)
    global __pool
    conn = __pool.get()
    # if not autocommit:
    #     conn.begin()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            # if not autocommit:
    except BaseException as e:
        # if not autocommit:
        cur.close()
        __pool.put(conn)
        raise
    else:
        __pool.put(conn)
    return affected


def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)


class Field(object):

    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键:
                    if primaryKey:
                        raise BaseException('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise BaseException('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey  # 主键属性名
        attrs['__fields__'] = fields  # 除主键外的属性名
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (
            tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__insert_no_primary__'] = 'insert into `%s` (%s) values (%s)' % (
            tableName, ', '.join(escaped_fields), create_args_string(len(escaped_fields)))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (
            tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. '
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    def findNumber(cls, selectField, where=None, args=None):
        ' find number by select and where. '
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    def find(cls, pk):
        ' find object by primary key. '
        rs = select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    def save(self, contain_primary=False):
        args = list(map(self.getValueOrDefault, self.__fields__))
        sql = self.__insert_no_primary__
        if contain_primary:
            args.append(self.getValueOrDefault(self.__primary_key__))
            sql = self.__insert__
        rows = execute(sql, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = execute(self.__update__, args)
        if rows != 1:
            logging.warning('failed to update by primary key: affected rows: %s' % rows)

    def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)
