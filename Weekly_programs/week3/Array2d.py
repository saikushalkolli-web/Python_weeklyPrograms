#24331A05D8
#2d mATRIX oPERATIONS
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
arr[1][2]=12
print(arr)
arr2=np.array([[11,12,13],[14,15,16],[17,18,19]])
arr2[2][1]=99
print(arr2)
a=np.add(arr,arr2)
print(a)
b=np.subtract(a,arr2)
print(b)
n=int(input("Enter a number to subtract:"))
result=b-n
print(result)
print("After slicing 1st row and 1st column of the array: ")
print(arr[0:2, 0:2])
for row in arr:
    print(row)
for col in arr2:
    print(col)
