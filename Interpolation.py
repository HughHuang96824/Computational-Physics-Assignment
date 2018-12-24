#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File that contains methods of linear and cublic spline fitting
"""
Created on Thu Oct 18 14:21:10 2018

@author: Yaojia Huang
"""

import LU_Decomposition as Mat
import numpy as np
import matplotlib.pyplot as plt



# The function takes x, y datasets and the freqency
# It shows the plot of the linear interpolation and return fitting points
def Linear_Interpolation(x , y, freq = 100, plot = True, label = "Linear Interpolation"):
    
    # List that will store fitting data
    x_fit = []
    y_fit = []
    
    for i in range(len(x)-1):
        
        # Create lists that stores fitting data in one interval
        start = x[i]
        end = x[i+1]
        x_interpo = np.linspace(start, end, int(freq * (end - start)))
        y_interpo = []
        
        # Loop over selected sites of the fitting function
        for j in range(len(x_interpo)):
            
            # Calculate y value and put it in the y_interpo list
            y_interpo.append(((x[i+1]-x_interpo[j])*y[i]+
                              (x_interpo[j]-x[i])*y[i+1])/(x[i+1]-x[i]))
        
        # Put fitting data within one interval to the general list
        x_fit = np.concatenate((x_fit, x_interpo))
        y_fit = np.concatenate((y_fit, y_interpo))
    
    if plot == True:
        # Plot the fitting function
        plt.plot(x_fit, y_fit, c = 'r', label = label)
            
    return x_fit, y_fit




# The function takes x, y datasets and the freqency
# It shows the plot of the cubic spline and return fitting points
def Cubic_Spline(x, y, freq = 100, plot = True, label = "Cubic Spline"):
    
    # Number of data points
    num = len(x)
    
    # Create a matrix and a vector. Will solve Ax = b
    A = np.zeros((num - 2, num))
    b = np.zeros(num-2)
    
    # Loop over the rows (get elements for the matrix)
    for i in range(num - 2):
        
        # Put the coesfficients of each equation in the row
        A[i][i] = (x[i+1]-x[i])/6
        A[i][i+1] = (x[i+2]-x[i])/3
        A[i][i+2] = (x[i+2]-x[i+1])/6
        
        # Put the constant of the equation in b
        b[i] = (y[i+2]-y[i+1])/(x[i+2]-x[i+1])-(y[i+1]-y[i])/(x[i+1]-x[i])
        
    # Assume boundary condition
    # Second derivatives of the first and last points are 0
    # So delete the first and the last column of the matrix
    # Now the matrix has dimension (num-2)*(num-2)
    A = np.delete(A, 0, 1)
    A = np.delete(A, -1, 1)
    
    # Solve the matrix equation
    # Sol is a list of derivatives of each data points
    # except for the first and last points
    Sol = Mat.Solve(A, b)
    
    # Put the boundary condition back
    #Sol.insert(0, 0)
    #Sol.insert(num, 0)
    Sol = np.insert(Sol, 0, 0)
    Sol = np.insert(Sol, -1, 0)
    
    # List that will store fitting data
    x_fit=[]
    y_fit=[]
    
    # For each interval between data points
    for i in range(num-1):
        
        # Create lists that stores fitting data in one interval
        start = x[i]
        end = x[i+1]
        x_cs = np.linspace(start, end, int(freq * (end - start)))
        y_cs = []
        
        # Loop over selected sites of the fitting function
        for j in range(len(x_cs)):
            # Calculate the parameters of the fitting function
            a = (x[i+1]-x_cs[j])/(x[i+1]-x[i])
            b = 1-a
            c = (a**3-a)*(x[i+1]-x[i])**2/6
            d = (b**3-b)*(x[i+1]-x[i])**2/6
            
            # Calculate y value and put it in the y_cs list
            y_cs.append(a*y[i]+b*y[i+1]+c*Sol[i]+d*Sol[i+1])
        
        # Put fitting data within one interval to the general list
        x_fit = np.concatenate((x_fit, x_cs))
        y_fit = np.concatenate((y_fit, y_cs))
    
    if plot == True:    
        # Plot the fitting function
        plt.plot(x_fit, y_fit, c = 'b', label = label) 

    return x_fit, y_fit
        

# For test purpose
if __name__ == "__main__":
    
    x = [-2.1, -1.45, -1.3, -0.2, 0.1, 0.15, 0.8, 1.1, 1.5, 2.8, 3.8]
    y = [0.012155, 0.122151, 0.184520, 0.960789, 0.990050, 0.977751, 0.527292, 0.298197, 0.105399,
         3.936690e-3, 5.355348e-7]
    
    plt.figure()
    plt.title("Linear Interpolation and Cubic Spline")
    Linear_Interpolation(x, y, 200)
    Cubic_Spline(x, y, 300)
    plt.legend()
    plt.show()
    
    
    ''' Check if the second derivative is constant '''
    # Estimate first derivative
    x , y = Cubic_Spline(x, y, 500, plot = False)
    length = len(x)
    derivative = []
    for i in range(length-1):
        derivative.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    
    # Estimate second derivative
    deriv_2 = []
    for i in range(length-2):
        deriv_2.append((derivative[i+1]-derivative[i])/(x[i+2]-x[i]))

    # Check wether the values of the second derivative
    # are constants between data points
    same_or_not = []
    for i in range(length-3):
        if (abs(deriv_2[i+1] - deriv_2[i]) < abs(0.05*deriv_2[i])):
            # True means the variation of the 2nd derivative is large
            # around this region. It may result from the fact that
            # two values are in different data point intervals
            same_or_not.append(True)
        else:
            same_or_not.append(False)

    print (same_or_not)
    # Check the percentage of True
    print (same_or_not.count(True)/len(same_or_not))
    
                
                
                
                
                
                
                
                
                
                
                
                
                