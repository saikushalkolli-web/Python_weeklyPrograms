#24331a05d8
import pandas as pd
data={"NAME": ["KUSHAL","JASWANTH","JERRY"],
      "AGE":[19,20,None],
      "CITY": ["HYD",None,"BZA"]
      }
file=pd.DataFrame(data)
file["NAME"].fillna("Unknown")
file["AGE"].fillna(0)
print("After cleaning DataFrame:")
print(file)
file["colleges"]="MVGR"
file.rename(columns={"AGE":"Years"},inplace=True)
print("Data after Modification: ")
print(file)
