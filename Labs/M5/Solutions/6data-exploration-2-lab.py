# -*- coding: utf-8 -*-
"""

Answers to lab on data exploration (part 2)

"""

import numpy as np
import pandas as pd
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
rcParams['figure.figsize'] = 8,6

#
# problem 2
#

# note the index_col=0 option
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',
                 index_col=0)

#
# problem 3
#

sns.scatterplot(x='F.Undergrad', y='Expend', data=df)
sns.regplot(x='F.Undergrad', y='Expend', data=df)

sns.scatterplot(x='F.Undergrad', y='Outstate', data=df)
sns.regplot(x='F.Undergrad', y='Outstate', data=df)

df['F.Undergrad.log'] = df['F.Undergrad'].apply(np.log10)
sns.regplot(x='F.Undergrad.log', y='Outstate', data=df)

# define new vars
df['perc.accept'] = (100. * df.Accept/df.Apps).round(0)
df['perc.enroll'] = (100. * df.Enroll/df.Accept).round(0)

sns.scatterplot(x='perc.accept', y='Outstate', data=df)
sns.regplot(x='perc.accept', y='Outstate', data=df)

# at more expensive schools, students are less likely to
# enroll if accepted
sns.scatterplot(y='perc.enroll', x='Outstate', data=df)
sns.regplot(y='perc.enroll', x='Outstate', data=df)

# More selective schools tend to be more expensive
sns.regplot(y='perc.accept', x='Outstate', data=df)

# More selective schools tend to have lower graduation rates (?)
# that is surprising
sns.scatterplot(x='perc.accept', y='Grad.Rate', data=df)
sns.regplot(x='perc.accept', y='Grad.Rate', data=df)

# More expensive schools tend to have lower graduation rates
sns.regplot(x='F.Undergrad', y='Grad.Rate', data=df)

#
# problem 4
#

# it doesn't appear that more selective public schools are more expensive
sns.scatterplot(y='perc.accept', x='Outstate', hue='Private', data=df)

# there is a weak trend showing more expensive public schools are a
# little more selective
sns.regplot(y='perc.accept', x='Outstate', data=df[df['Private'] == 'No'])

# the trend is stronger among private schools
sns.regplot(y='perc.accept', x='Outstate', data=df[df['Private'] == 'Yes'])

# new categorical variable
breaks = [0,65,80,100]
df['PhD_level'] = pd.cut(df['PhD'], 
		           include_lowest=True, bins=breaks,
		           labels=['low', 'medium', 'high'])

sns.scatterplot(y='perc.accept', x='Outstate', style='PhD_level', hue='PhD_level', data=df)

