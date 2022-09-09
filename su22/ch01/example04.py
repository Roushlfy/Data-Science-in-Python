#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 11:30
# @Author: xzxiao

thu_url = 'www.tsinghua.edu.cn'
print(thu_url)
print(thu_url[-1])  # 按索引输出第一个字符
print(thu_url[4:-7])  # 输出第4到第-7个字符
print(thu_url[0:])  # 截取所有字符
print(thu_url * 2)  # 输出字符串两次
str_list = thu_url.split('.')  # 按照“.”分割字符串
print(str_list)
print(thu_url.upper())  # 字母全部大写
print(thu_url.title())  # 单词首字母大写
print(thu_url.find('tsinghua'))  # 按字符串查找
ie_url = thu_url.replace('tsinghua', 'tsinghua.ie')
print(ie_url + "\n工业工程系欢迎您!")  # 用“\”转义
