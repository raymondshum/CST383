"""
Student Name: Raymond Shum
Class: CST383-30_22
Assignment: Lab: data exploration - two variables
Due Date: 8-Feb-22
"""

import numpy as np
import pandas as pd
from matplotlib import rcParams
import seaborn as sns

"""Configuration from lab solutions:"""
    
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

"""
Lab Begin:
"""

url ='https://raw.githubusercontent.com/grbruns/cst383/master/College.csv'
df = pd.read_csv(url)

df.info()
df.head(5)

"""
Create scatter plots to compare some of the variables.  
Here are some questions to help you get started.  Follow your curiosity.

    Do smaller colleges spend more?  (variables F.Undergrad and Expend)
    
    Do smaller colleges charge more?  (variables F.Undergrad and Outstate)
    
    Define two new variables: perc.accept and perc.enroll.  The first is the 
    percentage of students who accepted out of those who applied (use variables
    Accept and Apps).  The second is the percentage of students who enrolled 
    out of those where were accepted (use variables Enroll and Accept).
    
    Now use the new variables in scatter plots.  
    For example: are more selective colleges more expensive, generally?

For each scatter plot that you create, write something about the form/shape, 
the direction, and the strength.  Think about the possible meaning of the 
scatterplot.

Don't just stick to my suggestions, choose some of your own variables to 
explore.  Think of questions that you find interesting. 
"""

# Do smaller colleges spend more?
sns.scatterplot(
    x='F.Undergrad',
    y='Expend',
    data=df
    )

# Do smaller colleges charge more?
sns.scatterplot(
    x='F.Undergrad',
    y='Outstate',
    data=df
    )

df['perc.accept'] = df['Accept'] / df['Apps']
df['perc.enroll'] = df['Enroll'] / df['Accept']

sns.scatterplot(
    x='perc.accept',
    y='perc.enroll',
    data=df
    )

"""
Think of more questions and see if you can create plots to help understand 
them. For example, are more selective colleges more expensive?  Just create 
more scatterplots and explore them.  There are lots of things to pursue in the 
college data.
"""

# Are more selective schools more expensive?

# Create 'Selective' column
breaks = [0,.5,.75,1]
df['Selective'] = pd.cut(
    df['perc.accept'], 
    include_lowest=True, 
    bins=breaks, 
    labels=['high','medium','low']
    )

sns.boxplot(
    x='Selective', 
    y='Outstate', 
    data=df
    )
