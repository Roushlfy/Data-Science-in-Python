#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Time: 2022/09/09  08:48
# @Author: xzxiao

import pandas as pd
import matplotlib.pyplot as plt

# load sanitized data from csv
sanitized_df = pd.read_csv(
    "./data/Iris_sanitized.csv",
    usecols=[i for i in range(1, 7)])

sanitized_df.columns = [
    'Id', 'SepalLength', 'SepalWidth',
    'PetalLength', 'PetalWidth', 'Species']

# draw the histogram of group Species=2
species_2 = sanitized_df[sanitized_df['Species'] == 2]

plt.figure(figsize=(8, 6), num='Iris Hist Graph')

plt.subplot(221)
plt.title('Histogram of Sepal Length of Species 2')
plt.hist(
    species_2['SepalLength'],
    bins=20,
    density=True,
    edgecolor='black',
    linewidth='1.0'
)
plt.xlabel('Sepal Length(cm)')
plt.ylabel('Frequency')

plt.subplot(222)
plt.title('Histogram of Sepal Width of Veriscolor Iris')
plt.hist(
    species_2['SepalWidth'],
    bins=20,
    density=True,
    edgecolor='black',
    linewidth='1.0'
)
plt.xlabel('Sepal Width(cm)')
plt.ylabel('Frequency')

plt.subplot(223)
plt.title('Histogram of Petal Length of Veriscolor Iris')
plt.hist(
    species_2['PetalLength'],
    bins=20,
    density=True,
    edgecolor='black',
    linewidth='1.0'
)
plt.xlabel('Petal Length(cm)')
plt.ylabel('Frequency')

plt.subplot(224)
plt.title('Histogram of Petal Width of Veriscolor Iris')
plt.hist(
    species_2['PetalWidth'],
    bins=20,
    density=True,
    edgecolor='black',
    linewidth='1.0'
)
plt.xlabel('Petal Width(cm)')
plt.ylabel('Frequency')

plt.subplots_adjust(wspace=0.3, hspace=0.5)
plt.savefig("./figures/veriscolor_hist.png")
plt.show()


# draw the scatter plot of three iris species
# load data species-wise
setosa_data = sanitized_df[sanitized_df.Species == 1]
versicolor_data = sanitized_df[sanitized_df.Species == 2]
virginica_data = sanitized_df[sanitized_df.Species == 3]

# draw scatter plot
plt.title('Scatter Plot of Sepal Length and Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

s1 = plt.scatter(setosa_data['PetalLength'],
                 setosa_data['SepalLength'],
                 color='red', marker='.')
s2 = plt.scatter(versicolor_data['PetalLength'],
                 versicolor_data['SepalLength'],
                 color='orange', marker='x')
s3 = plt.scatter(virginica_data['PetalLength'],
                 virginica_data['SepalLength'],
                 color='blue', marker='+')

# add legend
plt.legend(
    (s1, s2, s3),
    ('setosa', 'versicolor', 'virginica'),
    loc='best')

plt.savefig('./figures/petal_sepal_length.png')
plt.show()

# analysis of data attributes
# calculate the correlation
df = pd.read_csv("./data/iris_sanitized.csv", usecols=[1, 2, 3, 4, 5, 6])

corr_matrix = df.iloc[:, 1:-1].corr(method='pearson')
print(corr_matrix)

# petal width is strongly correlated with petal length
# ignore petal width when further data analyzing
df.iloc[:, [0, 1, 2, 3, 5]].to_csv(
    "./data/iris_del_petalwidth.csv",
    encoding='utf-8')
