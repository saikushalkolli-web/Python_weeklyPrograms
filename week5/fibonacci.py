#24331A05D8
#fIBONACCI wITH aND wITHOUT uSING rECURSIONS

#With Recursion
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter a number: "))
print("Fibonacci Series: ")
for i in range(n):
    print(fib(i),end=" ")

#Without Recursion
n=int(input("Enter a number:"))
if(n==0):
    print(0)
else:
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
