#24331A05D8
#fINDING tHE sUM oF tHE eLEMETNS pRESENT iN tHE lIST
lst=[]
i=int(input("Enter the size of the list: "))
for x in range(i):
    lst.append(int(input("Enter {} number: ".format(x+1))))
print("Sum of the elements present in the list: ",sum(lst))


