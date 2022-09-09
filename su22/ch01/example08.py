#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 16:33
# @Author: xzxiao

def bmi_cal():
    score = int(input("请输入百分制成绩:"))

    if score < 0 or score > 100:
        print("请输入0到100之间的一个成绩")
    else:
        if score >= 90:
            print("A")
        elif score >= 77:
            print("B")
        elif score >= 67:
            print("C")
        elif score >= 60:
            print("D")
        else:
            print("F")


bmi_cal()
