#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 14:16
# @Author: xzxiao

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'FangSong'

source = np.loadtxt("data/iris_scatter.csv", delimiter=',')

plt.subplot(221)
plt.title('花萼长度直方图', fontproperties='FangSong', fontsize=12)
n, bin, patches = plt.hist(source[:, 0], bins=30)
plt.grid(linestyle='--')
plt.xlabel('花萼长度', fontproperties='FangSong', fontsize=10)
plt.ylabel('频数', fontproperties='FangSong', fontsize=10)
print("图1直方图向量n", n)
print("图1bin的区间范围", bin)

plt.subplot(222)
plt.title('花萼宽度直方图', fontproperties='FangSong', fontsize=12)
n, bin, patches = plt.hist(source[:, 1], bins=30)
plt.grid(linestyle='--')
plt.xlabel('花萼宽度', fontproperties='FangSong', fontsize=10)
plt.ylabel('频数', fontproperties='FangSong', fontsize=10)
print("图2直方图向量n", n)
print("图2bin的区间范围", bin)

plt.subplot(223)
plt.title('花瓣长度直方图', fontproperties='FangSong', fontsize=12)
n, bin, patches = plt.hist(source[:, 2], bins=30)
plt.grid(linestyle='--')
plt.xlabel('花瓣长度', fontproperties='FangSong', fontsize=10)
plt.ylabel('频数', fontproperties='FangSong', fontsize=10)
print("图3直方图向量n", n)
print("图3bin的区间范围", bin)

plt.subplot(224)
plt.title('花瓣宽度度直方图', fontproperties='FangSong', fontsize=12)
n, bin, patches = plt.hist(source[:, 3], bins=30)
plt.grid(linestyle='--')
plt.xlabel('花瓣宽度', fontproperties='FangSong', fontsize=10)
plt.ylabel('频数', fontproperties='FangSong', fontsize=10)
print("图4直方图向量n", n)
print("图4bin的区间范围", bin)

plt.savefig('data/exercise5-2.png')
plt.show()
