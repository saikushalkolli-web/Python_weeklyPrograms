#24331A05D8
#fINDING lARGEST aND sMALLEST nUMBER iN tHE lIST
lst=[]
i=int(input("Enter the size of the list: "))
for x in range(i):
    lst.append(int(input("Enter {} number: ".format(x+1))))
M=max(lst)
m=min(lst)
print("Largest number in the list: ",max(lst))
print("smallest number in the list: ",min(lst))