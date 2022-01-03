# -*- coding: utf-8 -*-
"""
NumPy arrays lab.
Enter your code below each comment

@author: Glenn Bruns
"""

import random
import numpy as np

# here is a list of the mileage (given in MPG) of students
# in my last class: 21.1, 26.6, 16.3, 33.7, 31.2, 52.0, 27.1
# create a NumPy array names 'mpg' from these values (use the given order)

# create a new array x that has the same length as mpg but
# every value is 25.0  (use the NumPy size property of mpg)

# print the mileage of the third student

# print the mileage of the last student

# print the mileage of the first to the third students

# print the mileage of every other student, starting with the first

# can you print the same mileages, but in reverse order?

# make a copy of mpg, named mpg2

# print the concatenation of mpg and mpg2

# print the data type (dtype) of mpg

# add 5.0 to every element of mpg2

# create a NumPy array 'miles' giving the distances each
# student has to travel to CSUMB.  The values are:
# 8.1, 5.4, 12.8, 42.1, 15.0, 22.2, 18.5

# the gallons used by a student in a round trip to CSUMB
# is the round-trip distance divided by miles-per-gallon.  Using vectorized
# operations, compute the number of gallons used by each student
# in a round trip to CSUMB.  Assign the result to variable 'gallons'.

# create a boolean array that is True for every
# element of gallons that is less than 1.  Assign it to variable 'low_gas'.

# use a boolean mask to get the values in gallons that are less than 1

# run the following line of code, which creates an array of a million
# random numbers between 0 and 1
x = np.array([random.random() for _ in range(10000000)])

# write a python loop to compute the sum of the values in x

# define a Python function named 'array_sum' that will return
# the sum of the specified NumPy array x

# time how long it takes for your function to sum the elements of
# the big array x you defined earlier
# hint: use %timeit

# now time how long it takes to do the same thing using np.sum
    
# write code to illustrate that slicing does not copy the input
# data

# if you still have time, learn about some of the "magic commands"
# available in IPython
# https://ipython.org/ipython-doc/3/interactive/magics.html

