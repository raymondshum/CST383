# -*- coding: utf-8 -*-
"""
Probability lab #4

@author: Glenn
"""

import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# 1
# You apply to 10 companies for a job, and each company offers
# jobs to 20% of (qualified) applicants.  Compute a sample of
# replies, using 0 for no offer, and 1 for offer.
np.random.binomial(1, 0.2, size=10)

# 2 
# Repeat the experiment 10,000 times, and record in an array
# the number of offers for each experiment.
results = np.array([np.random.binomial(1, 0.2, size=10).sum() for i in range(10_000)])

# 3
# Plot your vector from 2 as a bar plot, showing for each possible
# value 0-10, the fraction of experiments that resulted in that value.
# Use the bar() function of matplotlib for the bar plot.  It takes
# two arguments: an array of x locations for the bars, and the values
# for the bar heights.
p = np.bincount(results, minlength=11)/results.size
plt.bar(range(11),p)

# 4
# using your data from problem 3, create another graph, but this time,
# for value i (from 0-10) show the fraction of experiments in which
# the number of offers was less than or equal to i. The value for 10 should
# be 1.0.  (Hint: consider using function numpy.cumsum()).
plt.bar(range(11),np.cumsum(p))

# 5
# Create another plot as in part 3, but this time get your array 
# of values from  a call to function numpy.random.binomial().
np_res = np.random.binomial(11, 0.2, size=10_000)
p = np.bincount(np_res, minlength=11)/np_res.size
plt.bar(range(11),p)

# 6
# create another plot as in part 3, but this time get your array
# of values from calls to function scipy.stats.binom().  This
# function will give you the PMF of the binomial distribution, so
# you don't have to simulate a bunch of trials.
binom_res = binom.pmf(np.arange(11), 10, .2)
plt.bar(range(11), binom_res)

# 7
# If you have time, compute the probability of getting 2 job offers 
# after 8 applications, given the the probability of an offer in one
# application is 0.1.  Do this through simulation and through the
# use of scipy.stats.binom().
binom.pmf(n=8,k=2,p=.1)

