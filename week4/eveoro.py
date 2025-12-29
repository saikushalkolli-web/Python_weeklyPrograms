#24331a05d8
#Finding even and odd numbers
n=int(input("Enter a number: "))
eve=[]
odd=[]
ec=0
oc=0
for i in range(1,n+1):
    if(i%2==0):
        ec +=1
        eve.append(i)
    else:
        oc +=1
        odd.append(i)
print("Number of even numbers: ",ec)
print("The even numbers are: ",eve)
print("Number of odd numbers: ",oc)
print("The odd numbers are: ",odd)
