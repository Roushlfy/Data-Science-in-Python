#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/8 10:19
# @Author: xzxiao

import pandas as pd

# load data
# column index is [0], row index is [0]
data = pd.read_csv('data/Iris.csv', index_col=[0], header=[0])

# print the first 10 rows
print(data.head(10))

# sort according to the values in 'PetalLengthCm'
print(data.sort_values(by='PetalLengthCm'))

# select part of the data table
part = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

# print the max, min, mean, median, corr
print("max:\n", part.max())
print(part.min())
print(part.mean())
print(part.median())
print(part.corr())

# sort the data according to Species and print descriptive info
grouped = data.groupby(by='Species')
grouped_sum = grouped.sum()
grouped_max = grouped.max()
grouped_min = grouped.min()
grouped_mean = grouped.mean()
print(grouped_min)
print(grouped_max)
print(grouped_mean)
print(grouped_sum)
