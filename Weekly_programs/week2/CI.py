#24331A05D8
#fINDING cOMPOUND iNTREST
print("How much Loan do you want?")
P=int(input())
print("What is the rate of intrest for your loan?")
R=int(input())
print("How much time do you have to repay the loan?(Enter the values in years)")
T=int(input())
n=int(input("How many times the interest is being compounded per year?"))
I=(P*(1+R/(100*n))**(T*n))-P
print("Your total intrest to be paid: ",round(I,2))


