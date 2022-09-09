#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 10:49
# @Author: xzxiao

import numpy as np

arr = np.array([[8, 3, 2, 5],
                [6, 22, 15, 8],
                [36, 16, 20, 31]
                ])

max_col = np.max(arr, axis=0)  # the maximum of each column
mean_col = np.mean(arr, axis=0)  # the average of each column
print(max_col)
print(mean_col)

# sort the rows according to the 2-th column
sorted_arr = arr[arr[:, 1].argsort()]
print(sorted_arr)

# filter out elements that are larger than 20
lt_20 = arr[arr > 20]
print(lt_20)
