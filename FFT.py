#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 09:12:17 2018

@author: Yaojia Huang
"""

import numpy as np
import matplotlib.pyplot as plt

# f(x) = 4 for 3 < x < 5
def func(x):
    f = []
    for i in x:
        if i < 3 or i > 5:
            f.append(0)
        else:
            f.append(4)
    return f

# f(x) = (1/sqrt(2*pi))*e^(-x^2/2)
func2 = lambda x: (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)

# f(x) = 1 for -1 < x < 1
def func3(x):
    f = []
    for i in x:
        if abs(i) < 1:
            f.append(1)
        else:
            f.append(0)
    return f

# f(x) = 0.5 for -2 < x < 2
def func4(x):
    f = []
    for i in x:
        if abs(i) < 2:
            f.append(0.5)
        else:
            f.append(0)
    return f

# Receieve the fnctions used for convolution, the samping range and sample size
# Plot the convolution and return a list of data points of the convolution
def Convolute(func1, func2, sample_size, rang, plot = True, label = "Convolution"):
    
    # Specify range and step size
    start = -rang
    end = rang
    step = (end-start)/sample_size
    t = np.arange(start, end, step)
    
    # Determine how many zeros need to be padded
    # so that the sample size is 2^m
    pad = 2
    while pad < 2*sample_size:
        pad<<=1
        
    # Get data from two functions
    y1 = func1(t)
    y2 = func2(t)
    
    # Fast Fourier tranform the two functions
    # Zeroes are padded if the sample size is smaller than pad
    y1 = np.fft.fft(y1, pad)
    y2 = np.fft.fft(y2, pad)
    
    # Multiple the Fourier tranform together
    y3 = y1 * y2
    
    # Use invrse fast Fourier transform
    # Padded zeros are truncated
    y3 = (np.fft.ifft(y3) * step)[int(sample_size/2):int(3*sample_size/2)]
    
    # Take the real part
    y3 = np.real(y3)

    if plot == True:
        # Plot
        plt.plot(t, y3, label = label)
        plt.legend()
        
    return t, y3
    

# For test purpose
if __name__ == "__main__":
    
    # Plot convolution of func and func2
    plt.figure()
    Convolute(func2, func, 1000, 10)
    t = np.linspace(-10, 10, 1000)
    plt.title("Convolution of h(x) and f(x)")
    plt.plot(t, func(t), label = "h(x) = 4 (3<=x<=5),\n           0  otherwise")
    plt.plot(t, func2(t), label = r"f(x) = $\frac{1}{2\pi}e^\frac{-x^2}{2}$")
    plt.legend(prop={'size': 9})
    plt.show()
    
    # Plot convolution of func3 and func4
    plt.figure()
    Convolute(func3, func4, 1000, 6)
    t = np.linspace(-6, 6, 1000)
    plt.title("Convolution of h(x) and f(x)")
    plt.plot(t, func3(t), label = "h(x) = 1 (|x|<1),\n           0  otherwise")
    plt.plot(t, func4(t), label = "f(x) = 0.5 (|x|<2),\n           0  otherwise")
    plt.legend(prop={'size': 9})
    plt.show()
    
    



