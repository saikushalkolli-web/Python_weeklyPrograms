#24331A05D8
#fINDING rECUURENCE oF a lETTER pRESENT iN a wORD
text=input("Enter a word: ")
i=input("Enter a letter to find its reccurence: ")
x=text.count(i)
if(x>0):
    print(i,"has repeated ",x," times")
else:
    print(i," is not present in the word")