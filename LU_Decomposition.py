#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File that contains matrix operations and solvers
"""
Created on Thu Oct 18 14:17:59 2018

@author: Yaojia Huang
"""
import numpy as np

# The functions taks a square matrix and decomposes it into an
# upper and a lower triangular matrices. Return these two matrices
def LU_Decomp(A):
    
    nrow = len(A)
    
    # Initialise L and U matrices
    L = np.zeros((nrow, nrow))
    U = np.zeros((nrow, nrow))
    
    # The diagnoal elements of L are set to be 1
    np.fill_diagonal(L, 1)
    
    # Loop over rows
    for i in range(nrow):
        # Loop over columns
        for j in range(nrow):
            
            if i <= j: # if i <= j, then calculate the elements of U
                # Apply the formula in the nest three lines
                U[i][j] = A[i][j] - sum ( L[i][k] * U[k][j] for k in range(i) )
                    
            else:      # if i > j, then calculate the elements of L
                # Apply the formula in the nest four lines
                L[i][j] = A[i][j] - sum( L[i][k] * U[k][j] for k in range(j) )
                L[i][j] /= U[j][j]
                
    return L, U



# The functions taks a square matrix and returns its determinant
def Det(A):
    
    # Get the L and U matrices
    l, u = LU_Decomp(A)
    
    # Initialise determinant
    det = 1
    
    # Multiply every diagonal element of U
    for i in range(len(u)):
        det *= u[i][i]
        
    return det



# The function takes the L and U matrices and a vector
# returns the solution of the equation
def LU_Solve(L, U, b):
    
    dim = len(b)
    
    # L·y = b, U·x = y
    # Initialise x and y
    x = np.zeros(dim)
    y = np.zeros(dim)
    
    # Loop over every element of y
    for i in range(dim):
        # Apply formula to calculate the element of y
        y[i] = b[i] - sum( L[i][j] * y[j] for j in range(i) )
            
    # Loop over every element of x in revered order
    for i in reversed(range(dim)):
        # Apply formula to calculate the element of x
        x[i] = y[i] - sum( U[i][j] * x[j] for j in range(i+1, dim) )
        x[i] /= U[i][i]
        
    return x



# The function takes a sqaure matrix and a vector
# returns the solution of the equation.
# It has the same functionality of LU_Solve
def Solve(A, b):
    
    dim = len(b)
    
    # L·y = b, U·x = y
    # Initialise x and y
    x = np.zeros(dim)
    y = np.zeros(dim)
    
    # Get the L, U matrics
    L, U = LU_Decomp(A)
    
    # Loop over every element of y
    for i in range(dim):
        # Apply formula to calculate the element of y
        y[i] = b[i] - sum( L[i][j] * y[j] for j in range(i) )
            
    # Loop over every element of x in revered order
    for i in reversed(range(dim)):
        # Apply formula to calculate the element of x
        x[i] = y[i] - sum( U[i][j] * x[j] for j in range(i+1, dim) )
        x[i] /= U[i][i]
        
    return x



# The function takes a square matrix and returns its inverse matrix
def Inv_Mat(A):
    
    dim = len(A)
    
    # Set the identity matrix
    I = np.identity(dim)
    
    # Decompose A into L and U
    L, U = LU_Decomp(A)
    
    # Solve the matrix column by column
    # (note: the i-th row is equivalent to the i-th column in the
    # identity matrix, so rows are used for calculation for convenience)
    Sol = [LU_Solve(L, U, I[i]) for i in range(dim)]
        
    # The inverse matrix is the transpose
    # of Sol becasue the result obtained from
    # each iteration should be put as columns
    # instead of rows                               
    Sol = np.matrix(Sol).transpose()
    
    return Sol





# For test purpose
if __name__ == "__main__":
    
    A = [[75196.8, 38941.8, 19774.6, 9566.66, 3927.51], 
[40076, 20840.4, 10634.1, 5174.3, 2139.18], 
[21374.8, 11168.9, 5731.66, 2808.21, 1171.06], 
[11391.4, 5985.65, 3092.46, 1527.9, 644.154], 
[6038.12, 3192.89, 1662.5, 829.658, 354.611]]
    b =[-2162.55, -1189.66, -659.002, -367.619, -205.661]

    # Get L and U matrices
    x, y = LU_Decomp(A)
    print (x, y)
    
    # Multiply L and U to check if the product is the same as A
    print (np.matmul(x, y) == A, "\n\n")
    
    # Print the solution of the eqaution
    print (LU_Solve(x, y, b))
    # Check two methods give the same answer
    print (Solve(A, b) == LU_Solve(x, y, b))
    # Print the answer from numpy to check the validity of the functions
    answer = np.linalg.solve(A, b)
    
    n=5
    G = 0
    for i in range(n):
        G += answer[i]*(2**(n+1-i))/(n+1-i)
    
    G = (1-G)/2
    print (G)
        
        

    # Get the inverse
    inv = Inv_Mat(A)
    print (inv)
    # See the answer from numpy to check
    print (np.linalg.inv(A), '\n')
    # See whether the product gives identity matrix
    print (np.matmul(A, inv))