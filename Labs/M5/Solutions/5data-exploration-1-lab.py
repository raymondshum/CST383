# -*- coding: utf-8 -*-
"""

Code related to lab on data exploration (part 1)

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
# sns.set_context('notebook')   
# sns.set_context('paper')  # smaller
sns.set_context('talk')   # larger

# change default plot size
rcParams['figure.figsize'] = 9,7

#
# problem 2
#

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv")

#
# problem 4
#

df.info()
df.describe().round(1)

#
# problem 5
#

df.drop(['usid', 'fnlwgt'], axis=1, inplace=True)

#
# problem 6
#

df.head()

#
# problem 7
#

df.education_num.describe().round(1)

df.education_num.plot(kind='hist')
plt.xlabel('years of education')

#
# problem 8
#

# using histogram
df.education_num.hist()

# using barplot
df.education_num.value_counts().plot.bar()   # value_counts sorts by count
df.education_num.value_counts().sort_index().plot.bar()

#
# problem 9
#


sns.kdeplot(df.capital_gain)

plot = sns.kdeplot(df.capital_gain, bw=10)
plt.title('Density of capital gains')
plt.xlabel('Capital gains (US $)')
plot.savefig('capital-gains-density.png')

#
# problem 10
#

df.workclass.value_counts()

df.workclass.value_counts().plot.bar()

sns.countplot(y='workclass', data=df)
plt.title('Row counts by work class')

#
# problem 11
#

(df.sex.value_counts()/df.sex.size).plot.bar()
plt.title('Fraction of rows by sex')

# I don't see a good way to do this with seaborn
# except by first calculating the probabilities first

#
# problem 12
#

sns.countplot(y='marital_status', data=df)
plt.title('Row counts by marital status')
plt.ylabel('Marital status')

#
# problem 13
#

sns.countplot(y='education', data=df, color='darkred')

sns.countplot(y='occupation', data=df, color='darkred')

sns.countplot(y='native_country', data=df)

df.native_country.value_counts()[:12].apply(np.log10).plot.bar()
plt.title('Row counts by native country')
plt.ylabel('Counts (log10)')

