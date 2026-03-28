#24331A05D8
"""
Write a python program that takes the list of tuples and sorts the
list of tuples in increasing order by the last element in each tuple.
"""
Tuples=[(1,0),(0,0),(3,6),(9,4),(5,3)]
Sorted_list= sorted(Tuples,key=lambda x:x[-1])
print("Given tuples list: ",Tuples)
print("Sorted tuples list: ",Sorted_list)