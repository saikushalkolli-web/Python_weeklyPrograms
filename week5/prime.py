
#Without Recursion
n=int(input("Enter a number: "))
for i in range(2,n):
    if(n%i==0):
        print(n,"is not a prime number")
        break
else:
    print(n,"is a prime number")

#With Recursion
def prime(n,i=2):
        if(n<2):
            return False
        if(n==i):
            return True
        if n%i==0:
            return False
        return (n,i+1)

n=int(input("Enter a number: "))
if prime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

