#24331A05D8
#fACTORIAL wITH aND wITHOUT rECURSION

#Using Recursion
n=int(input("Enter a number to find its factorial: "))
res=1
for i in range(n,0,-1):
    res=res*i
print("The factorial of",n,"is: ",res)

#With Recusrion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number to find its factorial: "))
print("The factorial of ",n,"is: ",fact(n))
