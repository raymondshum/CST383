# -*- coding: utf-8 -*-
"""
Probability lab #6

@author: Glenn
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

plt.rcParams['figure.figsize'] = [4,3]
plt.rcParams['font.size'] = 10

# 6
def norm_plot(mean, sd):
    x = np.linspace(mean-3*sd, mean+3*sd)
    probs = norm.pdf(x, loc=mean, scale=sd)
    plt.plot(x, probs, color="darkred")
    plt.title('PDF of normal dist. with mean {} and SD {}'.format(mean, sd))
    
norm_plot(5, 0.5)

# 7
x = np.random.normal(5, 0.5, size=1000)
sns.distplot(x)

# 8

# part a
norm_plot(10, np.sqrt(0.04))

# part b
# A standard deviation is sqrt(0.04) = 0.2.  I expect 68% of
# the measurements to lie within 1 standard deviation of 10,
# so I expect 68% of the measurements to lie in [9.8, 10.2]

# part c
# Analytical solution: 0.4 meters is two standard deviations, so by the 68-95-99.7
# rule I expect 95% of the measurements to fall within 0.4 meters of the true distance.
#
# Simulation solution:

x = np.random.normal(10, 0.2, size=1000)
p = np.mean(np.absolute(x - 10.0) < 0.4)

# 9

# sample and plot histogram
x = np.random.normal(5, 0.5, size=1000)
plt.hist(x, bins=30, density=True)
# plot pdf of normal distribution
x = np.linspace(3, 7)
probs = norm.pdf(x, loc=5, scale=0.5)
plt.plot(x, probs)
