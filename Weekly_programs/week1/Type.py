#24331A05D8
#cONVERSIONS oF dATATYPES
num=int(input("Enter a number:"))
print(num,type(num),sep=",")
num=str(num)                                     #conversion of int datatype to string datatype
print("After typeconversion: ",type(num))
char=input("Enter a string:")
print(char,type(char),sep=",")
char=int(char)                                  #conversion of string datatype to int datatype
print("After typeconversion: ",type(char))
f=float(input("Enter a float:"))
print(f,type(f),sep=",")
nf=int(f)                                        #conversion of float datatype to int datatype
print(nf,type(nf),sep=",")
cars=["BMW",'PORSCHE','AUDI','MCLAREN']
cars.append("Aston Martin")
print(cars)
cars=tuple(cars)                                #conversion of list datatype to tuple datatype
print("After conversion: ",type(cars))
cars=[("BMW",1),('PORSCHE',2),('AUDI',3),('MCLAREN',4)]
cars=dict(cars)                                 #conversion of tuple datatype to dictionary datatype
print(type(cars))
print(cars["BMW"],cars["MCLAREN"])