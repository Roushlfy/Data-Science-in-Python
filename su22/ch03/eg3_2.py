#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/6 15:43
# @Author: xzxiao

class NoSolution(Exception):
    pass


def quadratic(a, b, c):
    """计算一元二次方程 a*x^2 + b*x + c = 0
    的解。如果a等于0，返回ZeroDivisionError.
    如果无实根，返回None，None。如果有实根，返回
    x1, x2.
    >>> quadratic(0,1,1)
    <BLANKLINE>
    二次项系数a不能为0
    >>> quadratic(1,1,1)
    方程无实根
    (None, None)
    >>> sol = quadratic(2,6,4)
    有2个不同的实根x1=-1.0, x2=-2.0
    >>> print(sol)
    (-1.0, -2.0)
    >>> x1, x2 = quadratic(1,2,1)
    有2个相同的解 -1.0, -1.0
    >>> assert x1 == x2
    >>> x1 == x2
    True
    """
    try:
        if a == 0:
            raise ZeroDivisionError
        d = b ** 2 - 4 * a * c
        if d < 0:
            print("方程无实根")
            return None, None
        elif d == 0:
            x = - b/(2*a)
            print(f"有2个相同的解 {x}, {x}")
            return x, x
    except ZeroDivisionError as e:
        print(e)
        print("二次项系数a不能为0")
    else:
        x1 = (- b + d ** 0.5) / (2 * a)
        x2 = (- b - d ** 0.5) / (2 * a)
        print(f"有2个不同的实根x1={x1}, x2={x2}")
        return x1, x2


quadratic(0, 1, 1)
quadratic(1, 1, 1)
sol = quadratic(2, 6, 4)
print(sol)
x1, x2 = quadratic(1, 2, 1)
assert x1 == x2
