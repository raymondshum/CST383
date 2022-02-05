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
rcParams['figure.figsize'] = 8,6

# read the data
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

# get an overview of the data
df.info()

#
# regression problem: predict a college's tuition
#

predictors = ['Top10perc', 'F.Undergrad']
target = 'Outstate'
X = df[predictors].values
y = df[target].values

# split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# scale the data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# build a kNN regressor
regr = KNeighborsRegressor()
regr.fit(X_train, y_train)

# make predictions
predictions = regr.predict(X_test)

# compare first ten predictions with first ten correct values
print(predictions[:10].astype(int))
print(y_test[:10])

# compute Mean Squared Error of predictions
mse = ((predictions - y_test)**2).mean()
print('MSE: {0:.0f}'.format(mse))

# plot absolute prediction error as a histogram
plt.figure(figsize=(8,6))
sns.distplot(predictions - y_test, kde=False)
plt.title('Histogram of prediction error')
plt.xlabel('Absolute difference between prediction and actual value ($)')
plt.xlim(-12000, 12000);
