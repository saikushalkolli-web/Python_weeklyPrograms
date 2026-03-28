#24331A05D8
#lIST aS aN aRGUEMENT tO tHE fUNCTION
def list_func (lst):
    print("Elements present in the list: ",end =" ")
    for i in lst:
        print(i,end=" ")
    print(sep=",")
    print("No.of elements present in the given list: ",len(lst))
lst=["AUDI",'MCLAREN','MERCEDES','FERRARI','PORSCHE']
list_func(lst)
