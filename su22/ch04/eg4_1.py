#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/7 09:29
# @Author: xzxiao


import numpy as np

# create a ndarray from a list of numbers
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr0 = np.array(numbers)
arr0.reshape((3, 3))
# print the descriptive info
print("rank:", arr0.ndim)
print("shape:", arr0.shape)
print("transpose:", arr0.T)
print("data type:", arr0.dtype)
print("number of elements:", arr0.size)
print()


# create a ndarray containing 12 elements via arrange()
arr1 = np.arange(1, 13, 1.0)
print("type: ", arr1.dtype)
print("shape: ", arr1.shape)
print()

# create a ndarray via linspace()
arr2 = np.linspace(0, 10, num=30, dtype='float')
print(arr2)
print()

# create a ndarray by func full()
arr3 = np.full((4, 5), 6)
print(arr3)
