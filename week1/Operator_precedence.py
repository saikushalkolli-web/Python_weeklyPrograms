#24331A05D8
#Checking the operator precedence
print(5+3*2)        # *operator is prioritized more than +
print(2*3**2)       # **(exponential) is prioritized more than *
print(2**3**2)      #As both are having same priority, right to left associativity takes place
print((2**3)**2)    #()parenthesis have the highest priority, so operations present in it would take place first