#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 15:59
# @Author: xzxiao

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

source = np.loadtxt("data/iris_scatter.csv", delimiter=',')

matplotlib.rcParams['font.family'] = 'FangSong'

x_values = source[:, 2]
y_values = source[:, 3]

plt.scatter(x_values, y_values,
            c='r', marker=4)
plt.xlabel('花瓣长度', fontproperties='FangSong', fontsize=10)
plt.ylabel('花瓣宽度', fontproperties='FangSong', fontsize=10)
plt.grid(linestyle='--')
plt.show()
