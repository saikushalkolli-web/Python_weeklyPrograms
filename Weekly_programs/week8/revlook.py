dict={"a":1,"b":2,"c":3,"d":4,"e":4}
key=4
for keys in dict:
    if dict[keys]==key:
        print("key with",key,"is: ",keys)
    else:
        print("No keys are present with that value.")