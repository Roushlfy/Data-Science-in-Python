#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 10:26
# @Author: xzxiao

import numpy as np
numbers = np.linspace(0, 20, num=30, endpoint=False)
arr_1 = numbers.reshape(10, 3)
arr_2 = arr_1[5:8, 1:4]
arr_3 = arr_1[1::2, 1:3]
arr_4 = arr_1[arr_1 > 10]
arr_5 = arr_1[3:9:3, 1:3]

print(arr_1)
print(arr_2)
print(arr_3)
print(arr_4)
print(arr_5)
