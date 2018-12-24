#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:46:55 2018

@author: Yaojia Huang
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import time

random.seed(12345)

N = 100000

'''
Question 1
Plot histogram of 100000 uniformly distributed values from 0 to 1
'''
# Get 100000 uniform distributed values from 0 to 1
x =[random.uniform(0, 1) for i in range(N)]

# Plot the histogram of the data
plt.figure()
plt.ylim(0, 1.4)
plt.title("Uniform Distribution of Variables from 0 to 1")
plt.xlabel("X")
plt.ylabel("pdf(X)")
n = plt.hist(x, 200, (0, 1), normed=True, label = "Histogram of random numbers")[0]

# Plot the true pdf
y = np.linspace(0, 1, 201)
plt.plot(y, [1 for i in y], label = "True PDF")
plt.legend()

# Standard deviation
print ('std for Q1:', np.sqrt(sum([(n[i]-1)**2 for i in range(200)])/199))



'''
Question 2
Generate variables who pdf is sin(x)/2 between 0 and pi
'''
start = time.time()

y = [np.arccos(1 - 2 * random.uniform(0, 1)) for i in range(N)]

end = time.time()
# Calculate the time taken to generate the variables
print('Time for Q2:', time.time()-start)

# Plot the histogram of the data
plt.figure()
plt.ylim(0, 0.7)
plt.title(r"Distribution of Variables from 0 to $\pi$")
plt.xlabel("Y")
plt.ylabel("PDF(Y)")
n = plt.hist(y, 200, (0, np.pi), normed=True, label = "Histogram of random numbers")[0]

# Plot the true pdf
y = np.linspace(0, np.pi, 201)
plt.plot(y, 0.5*np.sin(y), label = "P(Y)")
plt.legend()

# Standard deviation
print ('std for Q2:', np.sqrt(sum([(n[i]- 0.5*np.sin(y[i]))**2 for i in range(200)])/199))


"""
Question 3
Obtain samples that distributed according to
the pdf, P(y):           (2/pi) * sin^2(y)
Envelope function, f(y): (2/pi) * sin(y)
Normalised Envelope: n   (1/2) * sin(y)
"""

y = []              # List for sampled data
i = 0               # Number of accepted data
start = time.time()
while i < N:        # While the sample size is not enough
    
    # Pick randomly deviate Y according to the pdf
    # obtained by normalising the envelope function.
    Y = np.arccos(1 - 2 * random.uniform(0, 1))
    
    # Pick a value uniform distributed between 0 and 1
    u = random.uniform(0, 1)
    
    # If u is less than P(Y)/f(Y), accept Y
    if u <= np.sin(Y):
        y.append(Y)
        
        # Increment the number of sample
        i+=1
        
# Print the time taken      
print ('Time for Q3:', time.time()-start) 

# Plot the histogram of the sample
plt.figure()
plt.ylim(0, 0.85)
plt.title(r"Distribution of Variables from 0 to $\pi$")
plt.xlabel("x")
plt.ylabel("PDF(x)")
n = plt.hist(y, 200, (0, np.pi), normed=True, label = "Histogram of random numbers")[0]

# Plot the pdf that the vriables correspond to
y = np.linspace(0, np.pi, 201)
plt.plot(y, (2/np.pi)*np.sin(y)**2, label = "P(x)")
plt.legend()

# Standard deviation
print ('std for Q3:', np.sqrt(sum([(n[i]- (2/np.pi)*np.sin(y[i])**2)**2 for i in range(200)])/199))