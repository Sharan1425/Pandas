import pandas as pd
from pandas.core.frame import DataFrame

data = pd.read_csv("C:\\Users\\Sharanm\\Downloads\\stock_prices.csv")

# TO View the data
print(data)
print("Data Columns: ", data.columns)
print("No of rows and columns: ",data.shape)
print("First few columns from that data", data.head())
print("Last five columns from that data", data.tail())
print("Retrive specific row from that data", data.tail(1))
print("To print the data in range", data[0:3])
print(DataFrame(data)) # DataFrame prints the data in tabluar format
print("To print the specific column in data", data.Date)
print(data.index) #Prints the Indexrange of the data

# Operations with DataFrame
print(data['Temp'].max()) # to get max or min value from desired column
print(data['Temp'].min())
print(data.describe())  # describe funtion describes the whole data, i,e show mean, min, count, max

# Conditional operations
print(data[data.Temp <=30]) #prints the values which are lessthan 30


 