#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/8 08:55
# @Author: xzxiao

import numpy as np
import pandas as pd

# x values and index
x = [2, 4, 6, 2, 4, 8]
index_x = ['a', 'b', 'c', 'd', 'e', 'f']

# y values and index
y = [1, 3, 5, 1, 3, 7]
index_y = ['j', 'b', 'c', 'd', 'e', 'f']

# create two Series object
s1 = pd.Series(x, index=index_x)
s2 = pd.Series(y, index=index_y)

# perform sin function on both series
z = np.sin(s1) + np.sin(s2)

print(z)
