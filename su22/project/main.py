import pandas as pd

# 加载原始数据
data = pd.read_csv('data/cs-training.csv')

# 输出前10行数据
print("前10行数据:")
print(data.head(10))

# 输出描述性信息
print("描述性统计信息:")
print(data.describe())


# 处理数据

# 处理重复数据
data.duplicated(subset=None, keep='first')
dup_row = data.duplicated(keep=False)
print('\n重复的行:\t', dup_row.sum())

# 删除重行并将数据存至新的csv文件
data_del_dup = data.drop_duplicates(subset=None, keep='first', inplace=False)
data_del_dup.to_csv('data/del_dup.csv', index=False)

del data, data_del_dup, dup_row

# 缺失值分析与处理
# 加载删去重复行之后的数据集
df = pd.read_csv('data/del_dup.csv', index_col=[0])

# 输出含有缺失值总数
df_stat = df.describe().T
df_stat['null'] = len(df) - df_stat['count']
print("\n缺失值总数:\t", int(df_stat['null'].sum()))

# 输出韩缺失值的列，及该列缺失值个数
df_nan = df.isnull()
col_nan = df.isnull().sum()
col_nan_any = df.isnull().any()
print('\n各列缺失值个数:\n', col_nan)
print('\n有缺失值的列:\n', col_nan_any)

# 对于缺失值个数小于100个的列，直接删除该列缺失值所在行。
# 对于缺失值大于等于100的列，用列均值填充。
df.dropna(axis=0, how='')

# 异常值分析与处理
# 根据age和MonthlyIncome列筛除异常值所在行

# 绘制箱线图

# 数据特征分析
# 加载异常值处理后的数据

# 绘制年龄、月收入变量的直方图

# 输出各变量之间的相关系数矩阵


# 客户行用分析及模型评价
# 加载数据集

# 使用sklearn库建立逻辑回归分析

# 给出模型评分
