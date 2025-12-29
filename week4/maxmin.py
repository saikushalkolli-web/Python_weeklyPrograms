a=int(input("Enter value of A"))
b=int(input("Enter value of B"))
c=int(input("Enter value of C"))
if(a>b and a>c):
    print("{} is the largest number".format(a))
elif(b>a and b>c):
    print("{} is the largest number".format(b))
else:
    print("{} is the largest number".format(c))
if(a==b and b==c):
    print("All the numbers have same values")
