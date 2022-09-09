#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/8 10:49
# @Author: xzxiao

import pandas as pd

# load data from csv
df = pd.read_csv("./data/Iris.csv")

# write data into excel
df.to_excel(
    excel_writer="./data/Iris.xlsx",
    sheet_name='Sheet1')

# load data again form excel
de_excel = pd.read_excel(
    "./data/Iris.xlsx",
    index_col=[0],
    header=[0])

# print the data table
print(de_excel)
