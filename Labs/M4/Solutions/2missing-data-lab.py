# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:30:59 2017

Data acquisition examples and lab solutions

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
# Reading CSV data
#


#
# Lab solutions
#

# 1
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/airquality.csv")

# 2
df.head()

# 3
df.info()

# 4
df.isnull().sum().sum()

# 5
np.sum(df.isnull().sum(axis=1) > 0)

# 6
df.isnull().sum() / df.shape[0]

# 7
df.isnull().sum(axis=1) / df.shape[1]

# 8
x = df.isnull().sum() / df.shape[0]
x.plot.bar()
plt.title('Fraction NA values per column')

# 9
# It depends on the importance of the Ozone and Solar_R data.
# If they weren't too important, I would remove the columns.
# Another factor would be how important having every date would be.

# 10
df_cleanrows = df.dropna()
df_cleanrows.isnull().sum().sum()

# 11
df_cleancols = df.dropna(axis=1)

# 12
df_cleanrows.size
df_cleancols.size

# 13
col_meds = { c:df[c].median() for c in df.columns }
df_med = df.fillna(col_meds)

# 14
col_means = { c:df[c].mean() for c in df.columns }
df_mean = df.fillna(col_means)

# 15
