from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from datetime import datetime


def main():

    # write test logs
    with open('./test_data/test_history.txt', 'a') as f:
        f.write('\n\nCall of the main function at:\n')
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # load original data
    data = pd.read_csv('./data/cs-training.csv', index_col=[0])

    # print descriptive info
    pre_check(data)

    # delete duplicated rows
    data_del_dup = handle_duplicates(data)

    # handle missing values
    drop_nan = handle_missing(data_del_dup)

    # handle abnormal values
    del_abnormal = handle_abnormal(drop_nan)

    # analyze sanitized data
    data_analyze(del_abnormal)

    # print the correlation matrix
    print_correlation(del_abnormal)

    # use logistic regression model to predict
    # customers' behavior
    log_reg(del_abnormal)



# 数据预处理
def pre_check(data):
    """Print descriptive info.
    Take in a DataFrame object.
    Return None.
    """
    # 输出前10行数据
    # print the first 10 lines of data
    with open('./test_data/test_history.txt', 'a') as f:
        f.write("\nThe first 10 rows of data:\n")
        f.write(data.head(10).to_string())

    # 输出描述性信息
    # print descriptive info
    with open('./test_data/test_history.txt', 'a') as f:
        f.write("\nDescriptive info:\n")
        f.write(data.describe().to_string())


# 处理数据
# Data sanitizing

# 处理重复数据
# handle duplicates
def handle_duplicates(data):
    """Handle duplicated rows by deleting 
    duplicated rows.
    """

    data.duplicated(subset=None, keep='first')
    dup_row = data.duplicated(keep=False)

    with open('./test_data/test_history.txt', 'a') as f:
        f.write(f'\nDuplicated rows:\n{ dup_row.sum()}')

    # 删除重行并将数据存至新的csv文件
    # delete duplicated rows and save to a new csv file
    data_del_dup = data.drop_duplicates(subset=None, keep='first', inplace=False)
    data_del_dup.to_csv('./data/del_dup.csv')
    return data_del_dup


# 缺失值分析与处理
# deal with missing data
def handle_missing(df):
    """Handle missing data according to
    the rules in the document.
    """

    # 加载删去重复行之后的数据集
    # load the duplicate-removed dataset
    df = pd.read_csv('./data/del_dup.csv', index_col=[0])

    # 输出含有缺失值总数
    # print the sum of missing values
    df_stat = df.describe().T
    df_stat['null'] = len(df) - df_stat['count']
    with open('./test_data/test_history.txt', 'a') as f:
        f.write(f"\nTotal number of missing values:\n{int(df_stat['null'].sum())}")

        # 输出含缺失值的列，及该列缺失值个数
        # print columns that contains missing values
        # and the number of missing values column-wise
        df_nan = df.isnull()
        col_nan = df.isnull().sum()
        col_nan_any = df.isnull().any()
        f.write(f'\nThe number of missing values in each column:\n {col_nan.to_string()}')
        f.write(f'\nColumns that has missing values:\n {col_nan_any.to_string()}')

        # 对于缺失值个数小于100个的列，直接删除该列缺失值所在行。
        drop_nan = df.dropna(axis=0, subset='NumberOfDependents',how='any')
        # 对于缺失值大于等于100的列，用列均值填充。
        avg = {'MonthlyIncome': drop_nan['MonthlyIncome'].mean()}
        f.write(f'{0}'.format(avg['MonthlyIncome']))
        drop_nan.fillna(value=avg, inplace=True)

        # save data to a new csv file
        drop_nan.to_csv('./data/handle_missing.csv')

    return drop_nan


# 异常值分析与处理
# abnormal data analysis and processing
def handle_abnormal(df):
    """Handle abnormal data.
    Delete abnormal data according to the 'MonthlyIncome' column.
    """

    # 根据age和MonthlyIncome列筛除异常值所在行绘制箱线图
    plt.figure(figsize=(10,6), num='Box Graph of Age and MonthlyIncome')
    plt.subplot(121)
    plt.boxplot(df['Age'], labels=['Age'])

    plt.subplot(122)
    plt.boxplot(df['MonthlyIncome'], labels=['Monthly Income'])

    plt.subplots_adjust(wspace=0.5)
    plt.savefig('./figures/box_age_inc.png')
    plt.show()

    # 删除异常值
    # delete abnormal data
    sw_q1 = df['MonthlyIncome'].quantile(0.25)  # 计算上四分位数
    sw_q3 = df['MonthlyIncome'].quantile(0.75)  # 计算下四分位数
    sw_iqr = sw_q3 - sw_q1  # 计算四分位间距
    sw_low = sw_q1 - 1.5 * sw_iqr  # 计算下限
    sw_up = sw_q3 + 1.5 * sw_iqr  # 计算上限

    del_abnormal = df.query(f'MonthlyIncome > {sw_low} and\
                                    MonthlyIncome < {sw_up}')

    # 绘制删除异常数据后的MonthlyIncome直方图
    del_abnormal[['MonthlyIncome']].plot(
        title='Monthly Income Box Graph',
        kind='hist',
        density=False,
        color='yellow',
        edgecolor='black',
        linewidth='0.8',
        bins=30,
        grid=False)
    plt.savefig('./figures/hist_del_abnormal.png')
    plt.show()

    # 将删除异常值之后的数据存储至新的csv文件
    del_abnormal.to_csv('./data/sanitized.csv')

    return del_abnormal

# 数据特征分析
# data analysis

def data_analyze(data):
    """Take in data as a DataFrame object.
    Analyze the features of the data.
    Draw a histogram of Age and MonthlyIncome and save the graph.
    """
    # 绘制年龄、月收入变量的直方图
    # draw a histogram with Age and Monthly Income
    plt.figure(figsize=(12, 6), num='Age and Monthly Income Hist Graph')
    plt.subplot(121)
    plt.hist(
        data[['Age']],
        bins=30,
        density=False,
        edgecolor='black',
        linewidth='0.8',
        color='pink'
    )
    plt.xlabel('Age(years)')
    plt.ylabel('Frequency')

    plt.subplot(122)
    plt.hist(
        data[['MonthlyIncome']],
        bins=30,
        density=False,
        edgecolor='black',
        linewidth='0.8',
        color='pink'
    )
    plt.xlabel('Monthly Income(dollars)')
    plt.ylabel('Frequency')

    plt.savefig('./figures/hist_age_monthly_income.png')
    plt.show()


# 输出各变量之间的相关系数矩阵
# print the correlation matrix
def print_correlation(data):
    """print the correlation matrix of the given data
    as a DataFrame object
    """
    corr_matrix = data.corr(method='pearson')
    with open('./test_data/test_history.txt', 'a') as f:
        f.write("The correlation matrix of all variables:")
        f.write(corr_matrix.to_string())
    

# 客户行用分析及模型评价
# customer behavior analysis
# and regression model analysis

def log_reg(data):
    """use logistic regression model to predict customer behavior
    save the rate of accuracy of the model to a .txt file.
    return value: None
    """
    x = data.iloc[:, 1:]
    y = data['SeriousDlqin2yrs']

    # 为了验证模型的拟合效果，将对数据集分成训练集和测试集
    # divide the data into training set and testing set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # 建立逻辑回归模型,迭代次数上限500次
    # build a logistic training model
    # maximum iteration times: 500
    model_lr = LogisticRegression(max_iter=500)
    model_lr.fit(x_train, y_train)

    # 预测测试集
    # predict the testing set
    y_pred = model_lr.predict(x_test)

    # 给出模型评分,存储至txt文本文件
    # rate the logistic regression model, and save to .txt file
    with open('./data/model_accuracy.txt', 'w') as f:
        print('logistic regression accuracy(acc):\n', model_lr.score(x_test, y_test), file=f)
        print('prediction accuracy rate:\n', metrics.accuracy_score(y_test, y_pred), file=f)

    # 保存预测结果为csv文件
    # save results as csv files
    y_test.to_csv('./data/log_reg_test_results.csv')
    np.savetxt('./data/log_reg_pred_results.csv', y_pred,
            fmt='%0.1f', delimiter=',', newline='\n')


if __name__ == '__main__':
    main()
