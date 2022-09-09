#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/6 10:45
# @Author: xzxiao


from math import pi
from eg2_1 import triangle


# calculate the area of a circle
def area_circle(r):
    return pi * r * r


# calculate the area of a rectangle
def area_rect(a, b):
    return a * b


# if the current module is running
# the following code will be executed
if __name__ == '__main__':
    triangle()
    _a = float(input("请输入矩形第一条边长"))
    _b = float(input("请输入矩形第二条边长"))
    area_rect(_a, _b)
    _r = float(input("请输入圆半径"))
    area_circle(_r)
