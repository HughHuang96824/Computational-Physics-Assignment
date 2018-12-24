The files contain the assignments of Computational Physics. The assignment was completed in Python. In all files except for "Random Number", 
the required functionalities are realised in self-defined functions. The input for each function and the return type are specified below.
In "Random Number", the functionalities are not encapsulated because they are not very complicated; most work is done by hand before 
running the program. The user can just run the program to see all the results discussed in the write-up.



Machine Accuracy

epsilon(dtype = np.float , a = 2, b = 1):
The function calculates the epsilon of a given float type and return it




LU_Decomposition.py

This file contains methods for solving matrix

1.)LU_Decomp(A):
The functions takes a square matrix and decomposes it into an upper and a lower triangular matrices. The L and U matrices are returned.

2.)Det(A):
The functions takes a square matrix and returns its determinant.

3.)LU_Solve(L, U, b):
Solve LUx = b
The function takes the L and U matrices and a vector
It returns the solution of the equation.

4.)Solve(A, b):
The function takes a square matrix and a vector and returns the solution of the equation.
It has the same functionality of LU_Solve, but it is more compact and direct.

5.)Inv_Mat(A):
The function takes a square matrix and returns its inverse matrix.




Interpolation

1.)Linear_Interpolation(x , y, freq = 100, plot = True,label = "Linear Interpolation"):
It takes x and y lists and sampling frequency. It returns the values of the linear interpolation
The user can specify whether to plot the linear interpolation and its title.

2.)Cubic_Spline(x, y, freq = 100, plot = True, label = "Cubic Spline"):
It takes x and y lists and sampling frequency. It returns the values of the cubic spline.
The user can specify whether to plot the cubic spline and its title.




FFT

Convolute(func1, func2, sample_size, rang, plot = True, label = "Convolution"):
It takes two functions, expected sample size and the range of the samples. It returns the values of the convolution function. The user can specify whether to plot the convolution and its title.\




Random Number 
This file plots uniformly distributed variables and variables that has pdf(x) = 0.5sin(x) and pdf(x) = (2/pi)sin^2(x).
The histograms of these variables are plotted to show their distributions.
