num=int(input("Enter a number:"))
print(num,type(num),sep=",")
num=str(num)                                     #conversion of int datatype to string datatype
print("After typeconversion: ",type(num))
char=input("Enter a string:")
print(char,type(char),sep=",")
char=int(char)                                  #conversion of string datatype to int datatype
print("After typeconversion: ",type(char))