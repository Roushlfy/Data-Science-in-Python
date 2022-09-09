#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 13:49
# @Author: xzxiao

list_a = ['Java', [80, 90, 10], 'C', 'Python']

# 修改列表元素
list_a[2] = 'C++'
list_a.append('Php')
list_a[4:6] = ['Java', 'Database']
print(list_a)

# 在列表中插入序列
list_b = list_a[1]
list_b[1:1] = [85, 99]
print(list_a)

# 删除列表的元素
del list_a[5]
print('Python' in list_a)

# 列表操作函数
print('list_a的长度:', len(list_a))
print('list_b的最大值:', max(list_b))

# 返回新列表，原列表不变
print('输出 list_b * 2:', list_b * 2)
print('输出 list_a + list_b:', list_a + list_b)
