# -*- coding: utf-8 -*-
"""
Multidimensional NumPy arrays lab
Enter your Python code after each prompt.

@author: Glenn Bruns

Student Name: Raymond Shum
Due Date: 01-11-2022
Class: CST383
"""

import random
import numpy as np
import pandas as pd

# read student exam score data as a 2D NumPy array
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/sample-grades.csv").values

# print the score for the first student (row 0) and the third problem (column 2)
print(df[0,2])

# print all scores for student 15 (meaning row 15)
print(df[14])

# print all scores for problems 0-3
print(df[0:4])

# print all scores for problems 1, 5, 7
print(df[[0,4,7],:])

# assign the number of students to variable 'num_students'
num_students = df.shape[0]

# run the following command to get random data representing scores
# on two additional extra credit problems
ec = np.random.choice(np.array([0,1,2,3], dtype='int64'), size=num_students*2).reshape(num_students, 2)

# print the shape of ec
print(ec.shape)

# update df so that the two rightmost columns are the data in array ec
df = np.hstack([df,ec])

# print the mean value of all the scores
print(np.mean(df))

# print the number of scores > 2  (np.sum applied to a boolean mask will
# give the number of True values in the mask))
print(np.sum(df > 2))

# using a list comprehension, compute the total score for each student
# and assign the result to variable 'totals' as a NumPy array
totals = np.array([np.sum(row) for row in df])

# print the dtype of totals; it should be int64
print(totals.dtype)

# assign the number of columns to variable 'num_problems'
num_problems = df.shape[1]

# using a list comprehension, compute the average score for each
# problem and assign the result to variable 'prob_means' as a NumPy array
prob_means = [np.mean(df[:,prob]) for prob in range(num_problems)]

# what is the lowest of the average score values?
np.min(prob_means)

# Is it legal to subtract an array with shape (35,) from an
# array with shape (50,35)?  If so, what will happen?  Write
# your answer as a comment.
"""
Yes
The (35,) array is padded to (1,35)
Then (1,35) is expanded to (50,35)
Finally, (50,35) array is subtracted from (50,35) array.
Look at sample code underneath.
"""
sample = np.arange(50*35).reshape(50,35)
sample2 = np.arange(35)
result = sample - sample2

# the array (35,) will become (1,35), and will be subtracted
# from each row of the (50,35) array

# compute a new array df_centered, which is a 2D array with
# the same shape as df, but contains, for each column, the
# column values minus the average value for each column.
df_centered = df - prob_means

# What do you expect as the average values of the columns of
# dat_centered?  Print the result to find out.
print(np.mean(df_centered, axis=0))
print([np.mean(df_centered[:,i]) for i in range(num_problems)])

# consider extending idea about length of student trips, but make a matrix,
# where each row is a student, and 'mpg', 'miles' are columns.  In a separate
# array, show prices of gas at several gas stations.  

student = ["Ray", "Larry", "Nick", "Ian"]
mpg = [10.0, 40.0, 25.0, 30.0]
miles = [50.0, 20.0, 10.0, 15.0]

student_trips = np.zeros(4, dtype={'names':('student', 'mpg', 'miles'),
                                   'formats':('U10', 'f8', 'f8')})

student_trips['student'] = student
student_trips['mpg'] = mpg
student_trips['miles'] = miles

print(student_trips)
print(student_trips.dtype)

stations = ["G1", "G2", "G3", "G4"]
prices= [5.33, 4.00, 1.25, 2.37]

gas_info = np.zeros(4, dtype={'names':('name', 'price'), 
                              'formats':('U10', 'f8')})

gas_info['name'] = stations
gas_info['price'] = prices

print(gas_info)
print(gas_info.dtype)