#24331A05D8
#ASCII VALUE CONVERSIONS
char=input("Enter a charecter: ")
if len(char) >=2 or len(char)<=0:
    print("Invalid inputs given")
else:
    print("ASCII value of {} is:{}".format((char), ord(char)))
print("Exiting the loop!!!")
