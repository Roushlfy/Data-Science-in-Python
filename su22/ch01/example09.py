#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 16:33
# @Author: xzxiao

def print_mul_table():
    i = 1
    while i < 10:
        j = 1
        output_line: str = ""
        while j < 10 and j <= i:
            output_line += f" {j}*{i}={i*j}"
            j += 1
        i += 1
        print(output_line)


print_mul_table()
