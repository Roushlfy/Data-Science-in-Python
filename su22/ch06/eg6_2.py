#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/8 09:35
# @Author: xzxiao

import pandas as pd
data = [[17.73, 14.12, 960],
        [23.03, 3.33, 983],
        [1.78, 1.46, 1710],
        [2.94, 0.65, 55],
        [3.19, 0.67, 36]]

index_y = ['GDP', 'Pop', 'Area']
index_x = ['China', 'USA', 'Russia', 'France', 'UK']

df = pd.DataFrame(data=data, index=index_x, columns=index_y)

print(df['Pop']['China'])
print(df['GDP'])
print(df['Pop'])

print(df[df['GDP'] > 10])
print(df.iloc[1:4, 0:2])

df['GNP'] = [16.79, 23.37, 1.96, 2.96, 3.06]
print(df)

print(df[(df['GDP'] > 10) & (df['Area'] > 900)])

df.loc['UK', 'Area'] = 35.76
df.drop(columns='GDP', inplace=True)
print(df)
