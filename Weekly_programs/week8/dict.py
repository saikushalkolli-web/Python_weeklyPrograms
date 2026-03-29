#24331a05d8
Data={"Name":"HAN","age":"19","place":"BUSAN","sport":"Basketball"}
print("keys: ",Data.keys())
print("values: ",list(Data.values()))
print("items: ",Data.items())
Data.pop("age")
if "age" in Data:
    print("Age isn't popped yet")
else:
    print("Age has been popped")
    
