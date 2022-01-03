# -*- coding: utf-8 -*-
"""
Multidimensional NumPy arrays lab
Enter your Python code after each prompt.

@author: Glenn Bruns
"""

import random
import numpy as np
import pandas as pd

# read student exam score data as a 2D NumPy array
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/sample-grades.csv").values

# print the score for the first student (row 0) and the third problem (column 2)

# print all scores for student 15 (meaning row 15)

# print all scores for problems 0-3

# print all scores for problems 1, 5, 7

# assign the number of students to variable 'num_students'

# run the following command to get random data representing scores
# on two additional extra credit problems
ec = np.random.choice(np.array([0,1,2,3], dtype='int64'), size=num_students*2).reshape(num_students, 2)

# print the shape of ec

# update df so that the two rightmost columns are the data in array ec

# print the mean value of all the scores

# print the number of scores > 2  (np.sum applied to a boolean mask will
# give the number of True values in the mask))

# using a list comprehension, compute the total score for each student
# and assign the result to variable 'totals' as a NumPy array

# print the dtype of totals; it should be int64

# assign the number of columns to variable 'num_problems'

# using a list comprehension, compute the average score for each
# problem and assign the result to variable 'prob_means' as a NumPy array

# what is the lowest of the average score values?

# Is it legal to subtract an array with shape (35,) from an
# array with shape (50,35)?  If so, what will happen?  Write
# your answer as a comment.

# the array (35,) will become (1,35), and will be subtracted
# from each row of the (50,35) array

# compute a new array df_centered, which is a 2D array with
# the same shape as df, but contains, for each column, the
# column values minus the average value for each column.

# What do you expect as the average values of the columns of
# dat_centered?  Print the result to find out.

# consider extending idea about length of student trips, but make a matrix,
# where each row is a student, and 'mpg', 'miles' are columns.  In a separate
# array, show prices of gas at several gas stations.  
