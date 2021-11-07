from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

tree_entr = DecisionTreeClassifier(criterion='gini')
x_file = open("train_x.txt", 'r')
y_file = open("train_y.txt", 'r')
x_train = []
y_train = []
for i in range(1000):
    y = x_file.readline()[:-2]
    a = y_file.readline()
    y_train.append(int(a))
    x_train.append([float(x) for x in y.split(' ')])

x_file = open("test_x.txt", 'r')
y_file = open("test_y.txt", 'r')
x_test = []
y_test = []
for i in range(1000):
    y_test.append(int(y_file.readline()))
    x_test.append([float(x) for x in x_file.readline()[:-2].split(' ')])


X_train = np.asarray(x_train, dtype=object)
Y_train = np.asarray(y_train, dtype=object)
X_test = np.asarray(x_test, dtype=object)
Y_test = np.asarray(y_test, dtype=object)
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')
tree_entr.fit(X_train, Y_train)
pred = tree_entr.predict(X_test)
print()
print(accuracy_score(Y_test, pred))
