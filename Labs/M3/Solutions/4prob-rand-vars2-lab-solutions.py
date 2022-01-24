# -*- coding: utf-8 -*-
"""
Probability lab #4

@author: Glenn
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# 1
x = np.random.choice([0,1], size=10, replace=True, p=[0.8, 0.2])

# 2
offers = [ np.sum(np.random.choice([0,1], size=10, replace=True, p=[0.8,0.2])) for _ in range(10000) ]

# 3
counts = np.bincount(offers)
probs = counts/len(offers)
plt.bar(list(range(len(probs))), probs)

# 4
cdf = np.cumsum(probs)
plt.bar(list(range(len(probs))), cdf)

# 5
offers = np.random.binomial(10, p=0.2, size=1000)
probs = np.bincount(offers)/1000
plt.bar(np.arange(len(probs)), probs)

# 6
# note that binom inherits from scipy.stats.rv_discrete
probs = binom.pmf(np.arange(11), 10, 0.2)
plt.bar(np.arange(11), probs)


