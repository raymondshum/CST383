# -*- coding: utf-8 -*-
"""

Code related to KNN lecture 1 lab

"""

import numpy as np
import pandas as pd
from matplotlib import rcParams
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the very useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
# sns.set_context('notebook')   
# sns.set_context('paper')  # smaller
sns.set_context('talk')   # larger

# change default plot size
rcParams['figure.figsize'] = 4,4

# read the data
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

# get an overview of the data
df.info()

#
# classification problem: predict whether a college is public or private
#

# select predictor variables and target variable
predictors = ['Outstate', 'F.Undergrad']
target = 'Private'
X = df[predictors].values
y = (df[target] == 'Yes').values.astype(int)

# test/train split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# look at the scaled data
print(X_train[:10,:])

# build a kNN classifier
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

# make predictions
predictions = clf.predict(X_test)

# compare first ten predictions with first ten correct values
print(predictions[:10])
print(y_test[:10])

# compute accuracy
accuracy = (predictions == y_test).mean()
print('accuracy: {0:.3f}'. format(accuracy))

# try with k = 7 instead of the default value of 5
clf = KNeighborsClassifier(n_neighbors=7)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
accuracy = (predictions == y_test).mean()
print('accuracy: {0:.3f}'. format(accuracy))

