#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/6 09:31
# @Author: xzxiao

def triangle():
    a = float(input("输入三角形的第一个边长:"))
    b = float(input("输入三角形的第二个边长:"))
    c = float(input("输入三角形的第三个边长:"))
    if not form_triangle(a, b, c):
        print("不能构成三角形")
        return None
    else:
        return area_triangle(a, b, c)


# assert valid parameters
def form_triangle(a, b, c) -> bool:
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True


# calculate the area of a triangle
def area_triangle(a, b, c):
    p = (a + b + c) / 2
    mul = p * (p - a) * (p - b) * (p - c)
    ans = pow(mul, 0.5)
    print(ans)
    return ans


triangle()
