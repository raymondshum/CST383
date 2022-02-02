# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:30:59 2017

Data acquisition examples and lab solutions

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#
# Reading CSV data
#


#
# Lab solutions
#

# 5a - read excel data after exporting to CSV
dat = pd.read_csv("C:/Users/Glenn/Google Drive/CSUMB/Fall19/DS/lectures-labs/4data-prep-exploration/acquisition-and-cleaning/resources/Unemployment.csv", skiprows=7)

# 5b - read excel data directly
dat = pd.read_excel("C:/Users/Glenn/Google Drive/CSUMB/Fall19/DS/lectures-labs/4data-prep-exploration/acquisition-and-cleaning/resources/Unemployment.xls", header=7)

# 6 - read CSV data from a URL
dat = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/unemployment.csv")


