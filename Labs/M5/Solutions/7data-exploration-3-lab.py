# -*- coding: utf-8 -*-
"""

Code related to lab on data exploration (part 3)

"""

import pandas as pd
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
rcParams['figure.figsize'] = 8,6

#
# problem 2
#

# note the index_col=0 option
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

#
# problem 3
#

# add two derived features
breaks = df['F.Undergrad'].quantile([0,0.33, 0.66, 1.0])
df['Size'] = pd.cut(df['F.Undergrad'],
			   include_lowest=True, bins=breaks,
			   labels=['small', 'medium', 'large'])

df.Size.value_counts().plot.bar()

#
# problem 4
#

g = sns.FacetGrid(df, col='Size', height=4, aspect=0.8)
g.map(plt.scatter, 'PhD', 'Outstate', s=20, color="r")

#
# problem 5
#

sns.scatterplot(x='PhD', y='Outstate', hue='Size', data=df, s=50)

#
# problem 6
#

sns.scatterplot(x='PhD', y='Outstate', hue='Size', style='Size', data=df, s=55)

#
# problem 7
#

sns.catplot(y='Outstate', col='Size', data=df, kind='violin', height=4, aspect=0.7)

#
# problem 8
#

sns.catplot(y='Outstate', col='Size', data=df, kind='violin', inner='stick', height=4, aspect=0.7)

#
# problem 9
#

g = sns.FacetGrid(df, row='Size', height=2.5, aspect=1.8)
g.map(plt.hist, 'PhD', color="r")



#
# slide 5
#

sns.scatterplot(x='Outstate', y='perc.enroll', data=df, s=40)
plt.title('Perc. enrolled/accepted by tuition')
plt.xlabel('Out of state tuition ($)')

# showing public/private
sns.scatterplot(x='Outstate', y='perc.enroll', hue='Private', data=df, s=40)
plt.title('Perc. enrolled/accepted by tuition')
plt.xlabel('Out of state tuition ($)')

#
# slide 6
#

sns.regplot(x='Outstate', y='perc.enroll', data=df)
plt.title('Perc. enrolled/accepted by tuition')
plt.xlabel('Out of state tuition ($)')

#
# slide 7
#

# box plot with raw data (jitter needed here)
# color values gives a greyscale level
sns.set_context('talk')   
g = sns.boxplot(x="Grad.Rate", y="Selective", data=df)
sns.stripplot(x="Grad.Rate", y="Selective", data=df, color="0.4")

# single violin plot with raw data
g = sns.catplot(x="Grad.Rate", y="Selective", kind='violin', data=df)
sns.stripplot(x="Grad.Rate", y="Selective", color="k", data=df, size=3, ax=g.ax)

#
# slide 8
#

sns.violinplot(x="Selective", y="Grad.Rate", data=df, inner="stick")
plt.title('Graduation rate by selectivity')

#
# slide 9
#

# color markers by Public/Private
sns.scatterplot(x='Top10perc', y='Grad.Rate', data=df, hue='Private')

# color/type markers by Public/Private
sns.scatterplot(x='Top10perc', y='Grad.Rate', data=df, 
                hue='Private', style='Private')

# size markers by tuition
sns.scatterplot(x='Top10perc', y='Grad.Rate', data=df, size='Outstate')

#
# slide 10
#

sns.violinplot(x='Selective', y='S.F.Ratio', data=df, hue='Private', split=True)
plt.title('Student/Faculty ratio by selectivity')

#
# slide 11
#

# matplotlib subplots and seaborn
# see https://stackoverflow.com/questions/23969619/plotting-with-seaborn-using-the-matplotlib-object-oriented-interface

fig, axes = plt.subplots(1,3,figsize=(12, 4), sharey=True)
for i,sel in enumerate(['low', 'medium', 'high']):
    sns.distplot(df[df['Selective'] == sel]['Grad.Rate'], kde=False, ax=axes[i])
    axes[i].set_title('Selective='+sel)
plt.subplots_adjust(wspace=0.1)    # controls width between plots

sns.distplot("Grad.Rate", col="Selective", data=df)


#
# slide 12
#

# using facet grid for the example of the last slide
g = sns.FacetGrid(df, col='Selective', height=4, aspect=0.8)
g.map(plt.hist, 'Grad.Rate', color='darkred')


#
# slide 13
#

# facet grid with rows and columns
sns.set_context('notebook')   
g = sns.FacetGrid(df, row='Private', col='Selective')
g.map(plt.hist, "Grad.Rate")

sns.set_context('notebook')   
g = sns.FacetGrid(df, row='Private', col='Selective')
g.map(plt.scatter, "Grad.Rate", "Outstate", s=20, color='g')

#
# plots not used in slides
#

# violin plot combined with raw data, by category
sns.catplot(x="Private", y="Grad.Rate", col="Selective",
            data=df, kind="violin", inner="stick", height=5, aspect=0.6)

# histogram with raw data  (not very useful because of all the data)
sns.distplot(df['Grad.Rate'], hist=False, rug=True)

# strip plot by category
sns.catplot(x="Private", y="Grad.Rate", col="Selective",
            data=df, kind="strip", height=5, aspect=0.6)

# what is mean perc enroll by public/private?
# this is interesting: for private colleges, more selective ones
# have higher perc.enroll; for public colleges, less selective ones
# have higher perc.enroll.  However, the trend for private colleges
# is not strong.
sns.barplot(x='Private', y='perc.enroll', hue='Selective', data=df)

