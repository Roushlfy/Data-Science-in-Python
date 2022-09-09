#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 16:33
# @Author: xzxiao

# 元素正向索引和反向索引
tuple_a = ('Max', 28, 'Boston', ['apple', 'banana', 'cherry'])
print("age: ", tuple_a[1])
print("favorite_fruits: ", tuple_a[-1])

# 截取元素
tuple_num = (1, 2, 3, 2, 5, 2, 7, 8, 9, 10)
a = tuple_num[1:5:2]
b = tuple_num[::-1]
print(a, b, sep='\n')

# 修改元组中的可变元素
tuple_a[3].append('blueberry')
print(tuple_a)

# 元素计数与索引值
print("count 2: ", tuple_num.count(2))
print("the index of 2: ", tuple_num.index(2))

# 元组与列表互相转换
list_num = list(tuple_num)
print("list_num: ", list_num)
obj_num = tuple(list_num)
print("type of obj_num: ", type(obj_num))

# 元组解包
name, age, city, favorite_fruits = tuple_a
print(name, age, favorite_fruits, sep='\n')
