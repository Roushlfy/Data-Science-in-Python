#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Time: 2022/09/08  14/40
# @Author: xzxiao

import pandas as pd
import matplotlib.pyplot as plt

def func1():
    df = pd.read_csv("./data/Iris_0625.csv")
    df.info()

    # print the first 5 lines of the data table
    print("The first 6 lines:\n", df.head(6))

    # print the descriptive info
    print("Description Info:\n", df.describe())

    # print duplicated rows
    dup_row = df.duplicated(keep=False)  # row index
    print("Duplicated lines:\n", df[dup_row])
    print("Number of duplicated lines: ", dup_row.sum())

    # delete other duplicated rows
    dropped = df.drop_duplicates(
        keep='first'
    )

    # counting missing values
    mis_counts = dropped.isnull().sum(axis=1)
    total_mis = mis_counts.sum()
    print("Total number of missing values:\n", mis_counts[mis_counts > 0])
    print(total_mis)

    # use the average of each group to fill missing values
    grouped = dropped.groupby('Species')
    for x in grouped:
        values = x[1].mean().to_dict()
        x[1].fillna(value=values, inplace=True)
        dropped.update(x[1])
    # save data as iris_filled.csv
    filled = dropped
    filled.to_csv("./data/iris_filled.csv")


    # abnormal data analysis
    # draw box graph of each column
    plt.figure(figsize=(8, 6), num='Iris Box Graph')
    plt.subplot(221)
    plt.boxplot(filled['SepalLength'], labels=['Sepal Length'])

    plt.subplot(222)
    plt.boxplot(filled['SepalWidth'], labels=['Sepal Width'])

    plt.subplot(223)
    plt.boxplot(filled['PetalLength'], labels=['Petal Length'])

    plt.subplot(224)
    plt.boxplot(filled['PetalWidth'], labels=['Petal Width'])

    plt.subplots_adjust(wspace=0.2, hspace=0.25)
    plt.savefig("./figures/iris_box.png")
    plt.show()


    # abnormal data sanitizing
    sw_q1 = filled['SepalWidth'].quantile(0.25)  # calculate the upper quartile
    sw_q3 = filled['SepalWidth'].quantile(0.75)  # calculate the lower quartile
    sw_iqr = sw_q3 - sw_q1  # interquartile range
    sw_low = sw_q1 - 1.5 * sw_iqr  # calculate lower fence
    sw_up = sw_q3 + 1.5 * sw_iqr  # calculate upper fence
    delabnormal_data = filled.query(f'SepalWidth > {sw_low} and\
                                    SepalWidth < {sw_up}')

    # draw bx graph according to sanitized data
    delabnormal_data[['SepalWidth']].plot(kind='box', grid=False)
    plt.savefig('./figures/iris_sepalwidth_box.png')
    delabnormal_data.to_csv('./data/iris_sanitized.csv')

if __name__ == '__main__':
    func1()