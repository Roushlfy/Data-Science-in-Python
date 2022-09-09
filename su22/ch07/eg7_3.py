from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# 加载csv数据集，指定第一列为索引
# load data and set the 0-th column as index
df_data = pd.read_csv('ch07/data/iris_sanitized.csv',
                      index_col=[0])

# 将Species列赋值于y,为分类标号，其余列赋值给x,为属性集
# assign Species to y as markers
# assign other values to x as attribute set
x = df_data[['SepalLength', 'SepalWidth',
            'PetalLength', 'PetalWidth']]
y = df_data['Species']

# 将对数据集分成训练集和测试集
# divide dataset into training set and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


# 决策树模型
# decision tree model
model_dtc = DecisionTreeClassifier()
# 训练模型
# training
model_dtc.fit(x_train, y_train)
# 用模型用测试集
# use the model to predict testing set
y_pred = model_dtc.predict(x_test)

# 计算决策树分类模型的准确率
# calculate the accuracy of the decision tree model
print("决策树模型评分(acc):", model_dtc.score(x_test,
                                       y_test))
print('计算准确率(acc):', metrics.accuracy_score(y_test,
                                            y_pred))

# save results
y_test.to_csv('ch07/data/dt_test.csv')
np.savetxt('ch07/data/dt_pred.csv', y_pred,
           fmt='%0.1f', delimiter=',', newline='\n')


# 逻辑回归模型
# logistic regression model

# 加载csv数据集，指定第一列为索引
# load csv dataset (petalwidth ignored)
df_data = pd.read_csv('ch07/data/iris_del_petalwidth.csv',
                      index_col=[0])

# 将第一列数据取变量为y,是预测值，其余列为特征
# set the first column as y
# other columns values to be predicted
x = df_data[['SepalLength', 'PetalLength', 'PetalLength']]
y = df_data['Species']

# 为了验证模型的拟合效果，将对数据集分成训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# 建立逻辑回归模型,迭代次数上限500次
# build a logistic training model
# maximum iteration times: 500
model_lr = LogisticRegression(max_iter=500)
model_lr.fit(x_train, y_train)

# 预测测试集
# predict the testing set
y_pred = model_lr.predict(x_test)
print('逻辑回归模型评分(acc):\n', model_lr.score(x_test, y_test))
print('逻辑回归模型评分:\n', metrics.accuracy_score(y_test, y_pred))

# 保存预测结果
# save results
y_test.to_csv('ch07/data/lr_test.csv')
np.savetxt('ch07/data/lr_pred.csv', y_pred,
           fmt='%0.1f', delimiter=',', newline='\n')
