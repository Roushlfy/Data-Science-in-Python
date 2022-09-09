#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 10:36
# @Author: xzxiao

import numpy as np
mat_a = np.array([[1, 2, 1],
                  [2, -1, 3],
                  [3, 1, 2]
                  ])
mat_b = np.array([[7], [7], [18]])

inv_a = np.linalg.inv(mat_a)
det_a = np.linalg.det(mat_a)
a_dot_b = np.dot(mat_a, mat_b)

sol = np.linalg.solve(mat_a, mat_b)

print(inv_a)
print(det_a)
print(a_dot_b)
print(sol)
