# -*- coding: utf-8 -*-
"""
Probability lab #5

@author: Glenn
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

plt.rcParams['figure.figsize'] = [4,3]
plt.rcParams['font.size'] = 10

# 1
x = np.array([1,4,15])
probs = np.array([0.7, 0.28, 0.02])
plt.bar([1,2,3], probs, tick_label=x)
plt.title("PMF of random variable X")

# 2
ex = np.sum(np.dot(probs, x))
print("E(X) = {}".format(ex))

# 3
samp = np.random.choice(x, size=500, replace=True, p=probs)
samp.mean()

# 4
# About $2.  on average the value of the prize is $2.12

# 5
print("Estimated variance from sample = {:.2f}".format(samp.var()))
print("Estimated std. deviation from sample = {:.2f}".format(np.sqrt(samp.var())))

# 6
var = np.sum(np.dot(probs, np.square(x - ex)))
print("Variance of X = {:.2f}".format(var))

# 7
# the proof comes directly from the definition of expection:
# E(cX)
# = P(X = x_1)*(c*x_1) + P(X = x_2)*(c*x_2) + ... + P(X = x_n)*(c*x_n)
# = c*(P(X = x_1)*x_1 + P(X = x_2)*x_2 + ... + P(X = x_n)*x_n)
# = c*E(X)

# 8
num_trials = 1000
success_prob = 0.02
max_plot = 40  # very low probability of > 40 Yodas
probs = binom.pmf(np.arange(num_trials+1), num_trials, success_prob)
plt.bar(np.arange(max_plot+1), probs[:(max_plot+1)], color="darkred")
plt.title('Probability of number of Yodas in 1000 boxes')

# or, via simulation
def binom_sim_plot(num_trials, success_prob, num_samples=10000):
    x = np.random.binomial(num_trials, p=success_prob, size=num_samples)
    probs = np.bincount(x)/len(x)
    plt.bar(list(range(len(probs))), probs, color="darkred")
    plt.title('Bin({}, {}), simulated'.format(num_trials, success_prob))
    
binom_sim_plot(1000, 0.02)