#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 11:03
# @Author: xzxiao

import numpy as np
# create an int array from 2001 to 2022
arr_0 = np.arange(2001, 2023)
print(arr_0)

# use shuffle() to shuffle all elements in numbers
np.random.shuffle(arr_0)
print(arr_0)

# randomly pick three elements from arr_0
# replacement is allowed
arr_1 = np.random.choice(arr_0, 3, replace=True)
print(arr_1)
