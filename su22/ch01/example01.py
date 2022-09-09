#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 09:52
# @Author: xzxiao

def print_var(var_a):
    """输出对象的值及其3个属性
    """
    print("value:", var_a)  # 输出对象的值
    print("address:", id(var_a))
    print("type:", type(var_a))


var_str = 'Hello Python!'  # 创建一个str对象
print_var(var_str)
