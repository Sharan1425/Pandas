import pandas as pd

# Reading excel file
data = pd.read_excel("C:\\Users\\Sharanm\\Desktop\\Testing.xlsx", "Sheet1")
print(data)

# Writing to Excel File

data.to_excel("C:\\Users\\Sharanm\\Desktop\\ntest.xlsx", index=False, sheet_name="Surnames")

# Reading CSV File

df = pd.read_csv("C:\\Users\\Sharanm\\Downloads\\stock_prices.csv")
print(df)

# Writing to CSV file

df.to_csv("C:\\Users\\Sharanm\\Desktop\\Ntest.csv", index=False)

# We can manupulate the data cells by using converters parameter as below

def temp(cell):
    if int(cell) >= 35:
        return (cell,"High Temprature")
    return cell

df = pd.read_csv("C:\\Users\\Sharanm\\Downloads\\stock_prices.csv", converters={'Temp':temp})
print(df)

# we can combine the two Dataframes into one file by using ExcelWriter class
surnames = pd.read_excel("C:\\Users\\Sharanm\\Desktop\\Testing.xlsx", "Sheet1")
tem = pd.read_excel("C:\\Users\\Sharanm\\Desktop\\test.xlsx")

with pd.ExcelWriter("C:\\Users\\Sharanm\\Desktop\\Combine.xlsx") as writer:
    surnames.to_excel(writer,sheet_name="Surnames", index=False)
    tem.to_excel(writer,sheet_name="Weather Report", index=False)



