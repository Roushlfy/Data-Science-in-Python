#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/8 10:42
# @Author: xzxiao


import pandas as pd
import matplotlib.pyplot as plt


gdp_01_21 = pd.read_csv(
        "ch06/data/GDP_2001_2021.csv", 
        index_col=[0], header=[0])

# draw a line graph
years = [2001, 2005, 2009, 2013, 2017, 2021]
GDP = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
gdp_01_21.plot(kind='line',
               xticks=years,
               yticks=GDP,
               grid=True,
               xlabel='year',
               ylabel='quadrillion',
               title='GDP of 5 Main Countries (2001-2021)',
               style='1--')
plt.savefig("ch06/figures/GDP_2001_2021_line.png")
plt.show()


# read GDP_2021.csv
gdp_21 = pd.read_csv("ch06/data/GDP_2021.csv", index_col=[0], header=[0])
countries = ['China', 'USA', 'Russia', 'France', 'UK', 'Others']
gdp_21['GDP'].plot(
        kind='pie',
        subplots=True,
        autopct='%2.2f%%',
        legend=False,
        ylabel='',
        title='GDP Percentage of 5 Main Countries'
)
plt.savefig("ch06/figures/GDP_2021_pie.png")
plt.show()


# read GDP_POP_2021.csv
pop_21 = pd.read_csv(
        'ch06/data/GDP_Pop_2021.csv', 
        index_col=[0], usecols=['Country', 'GDP', 'Pop'])
countries = ['China', 'USA', 'Russia', 'France', 'UK']
items = ['GPD(quadrillion)', 'Population(100 million)']
pop_21 .index = countries
pop_21 .columns = items
pop_21 .plot(
        kind='bar',
        title='2021 GPD/population',
        style='2-',
        grid=True,
        rot=0)
plt.savefig('ch06/figures/GDP_POP_2021_bar.png')
plt.show()


# read iris_hist.csv
iris = pd.read_csv("ch06/data/iris_hist.csv", header=None)
iris.columns = [
        'Sepal Length(cm)', 'Sepal Width(cm)',
        'Petal Length(cm)', 'Petal Width(cm)']

iris.plot(
        x='Sepal Width(cm)',
        y='Sepal Length(cm)',
        kind='scatter',
        style='o')
plt.savefig("ch06/figures/iris_sepal_scatter.png")
plt.show()

iris.plot(
        x='Petal Width(cm)',
        y='Petal Length(cm)',
        kind='scatter',
        style='*')
plt.savefig("ch06/figures/iris_petal_scatter.png")
plt.show()

iris.plot(
        kind='box',
        title='Box Graph of Iris Length and Width')
plt.savefig("ch06/figures/iris_box.png")
plt.show()
