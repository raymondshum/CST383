# -*- coding: utf-8 -*-
"""
Probability lab #1

@author: Glenn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1
4/6

# 2
# simulate 1000 rolls of one die
# note: for sampling without replacement, use random.choice
x = np.random.randint(1, 6+1, size=10000)
# alternatives  (note that random.random_integers is deprecated)
x = np.random.choice([1,2,3,4,5,6], size=10000)
# to plot the distribution
sns.countplot(x)

# 3
# simulate 1000 rolls of two dice
x1 = np.random.randint(1, 6+1, size=1000)
x2 = np.random.randint(1, 6+1, size=1000)
x = x1 + x2

# 4
# replacement case: {11,12,13,...,44}
# no replacement case: {12,13,14,21,23,24,31,32,34,41,42,43}

# 5
# sample space is all finite sequences of values from 1-5
# sample space is the set of natural numbers (0,1,2,...)

# 9
# simulate rolling two dice until a 6 is rolled, many times
# each time, record the number of rolls to get a 6
k = 10000
x = np.array([0]*k)
for i in range(k):
    n = 1
    while np.random.randint(1, 6+1) != 6:
        n += 1
    x[i] = n
    
# how to do this in a vectorized way?
def num_rolls():
    n = 1
    while np.random.randint(1, 6+1) != 6:
        n += 1
    return n

x = np.array([num_rolls() for _ in range(100000)])

# a loopless way to do num_rolls:
def num_rolls2():
    max_rolls = 100
    x = np.random.randint(1, 6+1, size=max_rolls)
    indexes = np.flatnonzero(x == 6)
    if len(indexes) == 0:
        return max_rolls
    return indexes[0]

x = np.array([num_rolls2() for _ in range(100000)])

# no real difference
# in fact I think the version with two loops is fastest
%timeit num_rolls()
%timeit num_rolls2()

    
# histogram with matplotlib
plt.hist(x)

# histogram with seaborn
sns.distplot(x)
    

    
    
