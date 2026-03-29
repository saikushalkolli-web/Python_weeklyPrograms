#24331a05d8
import pandas as pd
file=pd.read_csv("test.txt")
print(file.head())
print("Tail of frame: ")
print(file.tail())
print("Information about frame: ")
print(file.info())
print("Description of frame: ")
print(file.describe())