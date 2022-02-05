import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns


# 2: Create a Python file in Spyder, and write code to load the data.  
url = 'https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv'
df = pd.read_csv(url)

# 3: Visually explore the data frame using the Variable explorer tab in Spyder, 
# which can be found in the upper right pane.

# 4: Which Pandas commands can you use to get a quick overview of the data?
df.info()
df.describe()
df.head()

# 5: Remove the 'usid' and 'fnlwgt' columns from the data frame.
df.drop(['usid', 'fnlwgt'], axis=1, inplace=True)

# 6: Use a Pandas command to look at the first rows of the data frame.
df.head()

# 7: The ‘education_num’ column records the number of years of education.  
# Use ‘describe’ to find min, max, median values for education_num.  
# Plot education_num using a histogram.  Label the x axis with 
# 'years of education'.

df['education_num'].describe()
chart = df['education_num'].hist()
chart.set_title('Histogram of education')
chart.set_xlabel('Years of education')
chart.set_ylabel('Count')

# 8: Does it make sense to use education_num with a histogram?  Try it, and 
# compare with a plot using a bar plot of the count of the rows by 
# education_num (as shown in lecture).

df['education_num'].value_counts().sort_index().plot.bar()

# 9: Plot capital_gain with a density plot.  Did you find anything interesting?
# Save your plot to a png file.

sns.kdeplot(df['capital_gain'], bw=0.5)

# 10: Investigate attribute ‘workclass’.  Plot it in an appropriate way.

df['workclass'].value_counts()
df['workclass'].head()

sns.countplot(y='workclass', data=df)

# 11: Use a bar plot to show the distribution of attribute ‘sex’.  Label the 
# 'Male' and 'Female' bars with the fraction of rows associated with each sex 
# (not a count).  Comment on what you find.  Why do you think the distribution 
# is like this?
(df['sex'].value_counts()/df['sex'].size).plot(kind='bar')

# 12: Use a horizontal bar plot to visualize attribute marital_status.
sns.countplot(y='marital_status', data=df)

# 13: If you have time, visualize all the attributes you haven’t explored yet.  
# Be sure to include 'native_country'.
df.info()

# 14: If you still have time, do single-variable visualization for the 
# attributes in the contribution campaign data.