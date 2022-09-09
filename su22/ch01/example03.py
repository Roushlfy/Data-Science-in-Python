#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 10:59
# @Author: xzxiao

x = int(input("输入第1个非零整数: "))
y = int(input("输入第2个非零整数: "))

print(f'{x} + {y} = ', x + y)  # 加法
print(f'{x} * {y} = ', x * y)  # 乘法
print(f'{x} ** {y} = ', x ** y)  # 乘方
print(f'{x} / {y} = ', x / y)  # 除法
print(f'{x} // {y} = ', x // y)  # 整除
print(f'{x} % {y} = ', x % y)  # 求余

print(f'{x} + 0.1 = ', x + 0.1)
print(f'{x} * 0.1 = ', x * 0.1)
