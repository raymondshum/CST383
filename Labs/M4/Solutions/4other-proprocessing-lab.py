# -*- coding: utf-8 -*-
"""

Code related to lecture slides on other preprocessing

"""

import numpy as np
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the very useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('notebook')   
# sns.set_context('paper')  # smaller
# sns.set_context('talk')   # larger

# change default plot size
rcParams['figure.figsize'] = 9,7

#
# 1
#

wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")

#
# 2
#

# so easy with DataFrame.sample!
df = wine.sample(20)
df.reset_index(inplace=True)

#
# 3
#

df = df.apply(zscore)

#
# 4
#

# one way
df.describe().loc['min']

# another way
df.apply(np.min, axis=0)

# another way
df.apply(pd.Series.min, axis=0)

#
# 5
#

df.apply(np.max, axis=0)

#
# 6
#

df = wine.sample(20)
df.reset_index(inplace=True)

def unit_scaling(x):
    return (x - x.min())/(x.max() - x.min())

df = df.apply(unit_scaling)

#
# 7
#

df.apply(np.min, axis=0)
df.apply(np.max, axis=0)

#
# 8
#

df = wine
df.corr()

#
# 9
#

# find max correlations using code
def most_corr_index(x):
    return x.sort_values(ascending=False).index[1]
def most_neg_corr_index(x):
    return x.sort_values().index[0]

# this gives, for each feature in the index, the 
# feature that is most correlated.
# It may seem counterintuitive, but just because
# feature x is the one most correlated with feature y,
# that does not mean feature y is the one most correlated
# with feature x.
df.corr().apply(most_corr_index)
df.corr().apply(most_neg_corr_index)

#
# 10
#

# note that you get a kind of free heat map if you
# save the output of corr() as a dataframe and look
# at it with the Spyder variable explorer

# another way to plot
corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns,
		     yticklabels=corr.columns)

#
# 13
#

n=10
sem_years = np.array([s+' '+str(y) for y in np.arange(14,19) for s in ['spring', 'fall']])
gpa = np.random.normal(loc=3, scale=0.5, size=(n,sem_years.size))
gpa = np.clip(gpa, 0, 4)
gpa = pd.DataFrame(gpa, columns=sem_years)
otter_ids = pd.DataFrame({'otter_id': np.random.randint(1000, 10000, n)})
gpa_by_semester = pd.concat([otter_ids, gpa], axis=1)

#
# 14
#
    