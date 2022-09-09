#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 10:34
# @Author: xzxiao
# 依次输入学生姓名、成绩，打印出姓名和成绩

name = input("请输入学生姓名：")
score = float(input("输入该生成绩："))

# 占位符格式化输出
print("%s 的成绩为 %.1f" % (name, score))

# 使用符字符串格式化输出
str_score1 = f"{name} 的成绩为 {score:.1f}"
print(str_score1)
