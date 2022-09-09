#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 11:03
# @Author: xzxiao

import numpy as np

contents = np.loadtxt('data/scores.csv', dtype=int, delimiter=',')
print(contents)

print("maximum of each column: ", np.max(contents, axis=0))  # print the maximum of each column
print("minimum of each column: ", np.min(contents, axis=0))  # print the minimum of each column
print("average of each column: ", np.mean(contents, axis=0))  # print the average of each column
print("variance of each column: ", np.var(contents, axis=0))  # print the variance of each column

print("average of each row: ", np.mean(contents, axis=1))  # print the average of each row

contents[:, 0] = np.sqrt(contents[:, 0])*10
contents[:, 0] = np.rint(contents[:, 0])

print(contents)  # print the modified score table

# sort the score table according to the average of each line
avg = np.mean(contents, axis=1)
print(avg)
index = avg.argsort()

# save the table to a new .csv filed
print(contents[index])
np.savetxt('data/sorted_scores.csv', contents[index], fmt='%d', delimiter=',')
