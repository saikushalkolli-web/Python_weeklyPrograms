#24331a05d8
Dict={"a":1,"b":2,"c":3,"d":4,"e":5}
key='r'
value=12
if key in Dict:
    print("Updating key"+key+" value"+ str(Dict[key])+"to"+str(value))
    str(value)
else:
    print("Adding key "+key+" Holding value "+str(value))
Dict[key]=value
print(Dict)