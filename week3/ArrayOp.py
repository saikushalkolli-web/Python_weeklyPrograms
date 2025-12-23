#24331A05D8
#uSING nUMpY aRRAYS AND oPERATIONS LIKE iNDEXING aND sLICING
import numpy as np
#Indexing
array= input("Enter numerical values(separated by spaces): ")
arr = np.array([int(x) for x in array.split()])                      #To have user defined input values.
print("Given array:", arr)
n=int(input("Enter an index number to see it's value: "))           #To Display the value asked by the user.
print(arr[n])
#Slicing
x=int(input("Enter start value to slice the array: "))
z=int(input("Enter end value to slice the array: "))
print("Sliced array: ",arr[x:z])
'''
Here even if the user gives negative values as -1 or -2 then the interpreter gives values from backwards
Slicing is used to print a specific part of the array depends on the user input as per the above problem.
'''
