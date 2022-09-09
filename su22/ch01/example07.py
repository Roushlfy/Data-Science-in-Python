#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/5 16:33
# @Author: xzxiao

# 直接赋值创建字典
dict_univ = {'10001': '北京大学',
             '10002': '中国人民大学',
             '10003': '清华大学',
             '10004': '北京交通大学',
             '10005': '北京林业大学'
             }

dict_univ['10006'] = '北京航空航天大学'  # 添加新元素
dict_univ['10005'] = '北京工业大学'  # 改变字典的值

buaa = dict_univ.pop('10001')  # 删除并返回一个键值对
print('buaa: ', buaa)

print(dict_univ['10003'])  # 通过key取值
print(dict_univ.get('10002'))  # 通过get方法取值
print(dict_univ.values())  # 输出全部的value
print(dict_univ.keys())  # 输出全部的key
