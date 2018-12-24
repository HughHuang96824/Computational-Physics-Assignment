#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File containing a function that get the machine epsilon of the system
"""
Created on Fri Oct 26 01:03:30 2018

@author: Yaojia Huang
"""

import numpy as np

# Function that retuns the machine epsilon
# It takes a number type as input
def epsilon(dtype = np.float , a = 2, b = 1):
    
    # Calculate the middle value between a and b
    middle = (dtype(a) + dtype(b)) / dtype(2)
    
    # If the middle value is the same as b
    if (middle == b): 
        # Return (a-1)
        return a - dtype(1)
    else: 
        # Else replacing "a" with "middle" and repeat the process
        return epsilon(dtype, middle, b)


# For test purpose
if __name__ == "__main__":

    theo_epsilon = [2**-23, 2**-52, 2**-63]
    ftype = [np.float32, np.double, np.longdouble]
    
    l = list(zip(theo_epsilon,ftype))
    
    # print the theoretical value, calculated epsilon and compare them
    for i in l:
        print (i[1])
        x = epsilon(i[1])
        print (x, i[0], x == i[0], "\n")