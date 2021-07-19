import pandas as pd
from sklearn import svm, metrics
import datetime

begin_time = datetime.datetime.now()
df1 = pd.read_csv('../../data/datatest.csv').drop(['sn', 'date'], axis=1)
df2 = pd.read_csv('../../data/datatest2.csv').drop(['sn', 'date'], axis=1)
df_train = pd.read_csv('../../data/datatraining.csv').drop(['sn', 'date'], axis=1)
df_test = df1.append(df2)

x_train = df_train.iloc[:, 0:5]
x_test = df_test.iloc[:, 0:5]
y_train = df_train['Occupancy']
y_test = df_test['Occupancy']

clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred)
recall = metrics.recall_score(y_test, y_pred)
f1_score = metrics.f1_score(y_test, y_pred)
print('Accuracy: ' + str(accuracy))
print('Precision: ' + str(precision))
print('Recall: ' + str(recall))
print('F1 Score: ' + str(recall))

completion_time = datetime.datetime.now() - begin_time
print('Completion time: ' + str(completion_time))
