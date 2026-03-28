#24331A05D8
#Program to show the number and it's square in the same list.
first=int(input("Enter the first number: "))
last=int(input("Enter the last number: "))
new_tup=[(i,i**2)for i in range(first,last+1)]
print("New tuple list: ",new_tup)
