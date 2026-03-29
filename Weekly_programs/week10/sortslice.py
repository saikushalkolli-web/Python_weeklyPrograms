#24331a05d8
import pandas as pd
data={"NAME": ["KUSHAL","JASWANTH","JERRY"],
      "AGE":["19","20","18"],
      "CITY": ["HYD","VSKP","BZA"]
      }
file=pd.DataFrame(data)
print("sort b ages: ")
print(file.sort_values(by="AGE"))
print("First row: ",file[:1])
print("Only names: \n")
print(file["NAME"])