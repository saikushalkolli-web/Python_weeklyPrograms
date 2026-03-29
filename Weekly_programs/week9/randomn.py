#24331a05d8
import random
file=open("test.txt","w")
for i in range(20):
    num=random.randint(1,100)
    file.write(str(num)+"\n")
file.flush()
file.close()
with open("test.txt","r") as file:
    print("Data present in the file: ")
    print(file.read(),sep=" ")
file.close()
