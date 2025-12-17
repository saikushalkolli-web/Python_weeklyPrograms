#24331A05D8
#Using Ravel function
#Defining NumPy
'''
NumPy is a Python library for fast numerical computing, built for optimizing the usage of powerful multidimensional arrays.
Before the creation of NumPy, Python was relied on lists for numerical data, lists are slow as they store elements in an individual order
and also require loops for mathematical operations. so Numeric and Numarray had been created to solve this issue, but they had their own
limitations. Then in 2005, Travis Oliphant created "NumPy" which includes all the functions of Numeric and Numarray and other funtions,
creating a library which can solve scientific computations and more.
'''
import numpy as npd
array=([[1,2,3],[4,5,6],[7,8,9]])
change=npd.ravel(array)
print("Before using ravel function: ",array)
print("After using ravel function: ",change)
