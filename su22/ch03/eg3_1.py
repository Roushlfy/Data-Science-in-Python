#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/6 14:51
# @Author: xzxiao

file_name = "data/2021012356.csv"
new_file = open(file_name, mode='w')
for i in range(0, 5):
    number = input("学号:")
    name = input("姓名:")
    gender = input("性别:")
    score = input("成绩:")
    new_file.writelines(number + ','
                        + name + ','
                        + gender + ','
                        + score + "\n"
                        )
new_file.close()

with open(file_name, mode='r') as read_file:
    contents = read_file.readlines()
    for line in contents:
        print(line)
