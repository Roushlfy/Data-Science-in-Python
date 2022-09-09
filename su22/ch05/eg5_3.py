#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 15:59
# @Author: xzxiao

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['font.family'] = 'STSong'

x_values = [0, 1, 2, 3, 4]
x_tickes = ['中国', '美国', '俄罗斯', '法国', '英国']
gdp_values = [17.73, 23.03, 1.78, 2.94, 3.19]
plt.bar(x_values, gdp_values, align='center', color='blue')
plt.ylabel('GDP(万亿美元)', fontproperties='STSong')
plt.title('部分国家2021年GDP数据', fontproperties='STSong')
plt.ylim(0, 25)
plt.xticks(x_values, x_tickes)

for x, y in enumerate(gdp_values):
    plt.text(x, y + 100, '%.1f' % round(y, 1), ha='center')

plt.show()
