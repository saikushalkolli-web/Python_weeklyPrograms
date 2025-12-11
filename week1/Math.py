#24331A05D8
#uSING mATH fUNCTIONS
import math                     #For math functions we need to import math library
#Area of the circle
r=float(input("Enter radius of the circle: "))
area=math.pi*r*r
print("Area of the circle: ",area)
#Roots of the equation
a,b,c=map(int,input("Enter the quadratic equation values of a,b,c: ").split())
discriminant=b**2-4*a*c
if(discriminant>0):
    root1= (-b+math.sqrt(b**2-4*a*c))/2*a
    root2= (-b-math.sqrt(b**2-4*a*c))/2*a
    print("Given quadratic equation:{}x^2+{}x+{} ".format(a,b,c) )
    print("Roots of the given equation: ",root1,root2)
elif(discriminant==0):
    root=-b/(2*a)
    print(root)
else:
    print("Discriminant of the given equation is less than 0, can't be calculated.")
#Quiz to find the values of sin90 and cos90
val1=int(input("Enter the value of sin90: "))
if(val1==1):
    print("You've entered the correct value")
    val2=int(input("Enter the value of cos90: "))
    if(val2==0):
        print("You've entered the correct value...")
        print("End of quiz")
    else:
        print("You've entered the wrong value")
else:
    print("You've entered the wrong value")
    print("End of quiz")