# -*- coding: utf-8 -*-
"""

Code related to lecture slides on bad data

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

#==============================================================================
# read the data
#==============================================================================

infile = "https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv"
df = pd.read_csv(infile)

#
# Problem 3
#

df.info()

#
# Problem 4
#

df.isna().sum()         # NAs per column
df.isna().sum().sum()   # total number of NAs

#
# Problem 5
#

# Inspecting visually I only see nan values

# using code to help
# I would expect that, among cities, if there was some
# "sentinel value" used to indicate missing information
df.contbr_city.value_counts().head(n=20)

# Oh, I found three interesting values here: None (I guess
# meaning not employed), "information requested per best
# efforts", meaning perhaps that the contributor refused,
# and "information requested", similarly.)
df.contbr_occupation.value_counts().head(n=20)

df.contbr_zip.value_counts().head(n=20)

# Get top value for each variable
df.apply(lambda x: x.value_counts().index[0])

#
# Problems 6 and 7 
#

# again, there are several interesting NA-like values:
# NOT EMPLOYED, RETIRED, NONE, INFORMATION REQUESTED.
# Also, some values appear to be variants of the
# same thing.
df.contbr_employer.value_counts().head(n=20)

#
# Problem 8
#

# number of memo_cd values
len(df.memo_cd.unique())

# what are the values?
df.memo_cd.value_counts()

# which fraction of the values are empty?
df.memo_cd.isnull().mean()

#
# Problem 9
#

# Pandas
df.contb_receipt_amt.plot.hist()
plt.title('Histogram of contribution amounts')
plt.xlabel('Contribution amount (US dollars)')
plt.ylabel('Count')

# Seaborn
sns.distplot(df.contb_receipt_amt)
plt.title('Histogram of contribution amounts')
plt.xlabel('Contribution amount (US dollars)')
plt.ylabel('Count')

# matplotlib
plt.hist(df.contb_receipt_amt.values)
plt.title('Histogram of contribution amounts')
plt.xlabel('Contribution amount (US dollars)')
plt.ylabel('Count')

#
# Problem 10
#

# easiest way to get the range of values
# I see that there are negative values.
df.describe()

# are the negative and positive values paired?
# I assume this would be through the same contributor
df_neg = df[df.contb_receipt_amt < 0][['contbr_nm', 'contb_receipt_amt']]

# this is interesting: many of the negative contributions are -2700
df_neg.contb_receipt_amt.value_counts()

# are there the same number of 2700 and -2700 contributions?  No.
temp = df[df.contb_receipt_amt.abs() == 2700.0][['contbr_nm', 'contb_receipt_amt']]
temp.contb_receipt_amt.value_counts()

#
# Problem 11
#

df.contbr_zip.str.len().value_counts()

#
# Problem 12
#

# this distribution doesn't look too unusual in itself.
# Perhaps surprising that there are many very short
# employer names, and also that there are more employer
# names of 35 than 25 or 30, but this may reflect that
# you are limited to 35 characters, and many names are
# longer.
df.contbr_employer.str.len().hist()

#
# Problem 13
#

contb_min = df.contb_receipt_amt.min()
contb_max = df.contb_receipt_amt.max()
df['amt1'] = (df.contb_receipt_amt - contb_min)/(contb_max - contb_min)

df.amt1.describe()

# distribution is interesting
df.amt1.hist()

# raw distribution
df.contb_receipt_amt.describe()
df.contb_receipt_amt.hist()

# look in more detail at values between 0 and 500 dollars
df[(df.contb_receipt_amt > 0) & (df.contb_receipt_amt < 500)].contb_receipt_amt.hist()

#
# Problem 14
#

# this helps in visually scanning the data
df_memo = df[['memo_cd', 'memo_text']]

# what memo_text values are associated with memo_cd values of X?
df[df.memo_cd == 'X'].memo_text.value_counts()

# how does this compare to the memo_text values when memo_cd is not X?
df[df.memo_cd.isnull()].memo_text.value_counts()

# from the above I gather that X is used when the contribution
# is not earmarked.  However, X does not appear to be used for
# only earmarked contributions

# are any memo_text values shared between the two cases of memo_cd?
# https://stackoverflow.com/questions/18079563/finding-the-intersection-between-two-series-in-pandas
memo_x    = df[df.memo_cd == 'X'].memo_text.unique()
memo_notx = df[df.memo_cd.isnull()].memo_text.unique()
set(memo_x) & set(memo_notx)

# so, only one non-NA value is in the intersection

# I found this on the web
df.groupby(['memo_cd', 'memo_text']).size().reset_index().rename(columns={0:'count'})
