#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xm1230
# datetime:2019/3/12 20:42
# software: PyCharm


class Rational:
    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            _um, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        gcd = Rational._gcd(num, den)
        self._num = sign * (num // gcd)
        self._den = den // gcd

    @staticmethod
    def _gcd(m, n):
        if n == 0:
            n, m = m, n
        while m != 0:
            m, n = n % m, m
        return n

    def num(self):
        return self._num

    def den(self):
        return self._den

    def __add__(self, other):
        num = self._num * other.den() + self._den * other.num()
        _den = self._den * other.den()
        return Rational(num, _den)

    def __sub__(self, other):
        _num = self._num * other.den() - self._den * other.num()
        _den = self._den * other.den()
        return Rational(_num, _den)

    def __mul__(self, other):
        return Rational(self._num * other.num(), self._den * other.den())

    def __floordiv__(self, other):
        if other.num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * other.den(), self._den * other.num())

    def __eq__(self, other):
        return self._num * other.den() == self._den * other.num()

    def __lt__(self, other):
        return self._num * other.den() < self._den * other.num()

    def __gt__(self, other):
        return self._num * other.den() > self._den * other.num()

    def __str__(self):
        return str(self._num) + '/' + str(self._den)

    def print(self):
        print(str(self._num) + '/' + str(self._den) + '=' + str(self._num / self._den))


class F:
    def f(self):
        self.g()

    def g(self):
        print('F.g called')


class C(F):
    def g(self):
        print('C.g called')


if __name__ == '__main__':
    # r = Rational(3, 5)
    # r2 = Rational(4, 5)
    # print(r2 > r)
    # print(r)
    # r.print()
    f = F()
    f.g()
    f.f()
    c = C()
    c.g()
    c.f()
