char=input("Enter a charecter: ")
if len(char)!=1:
    print("Invalid inputs given")
else:
    print("ASCII value of {} is:{}".format(char, ord(char)))
print("Exiting the loop!!!")