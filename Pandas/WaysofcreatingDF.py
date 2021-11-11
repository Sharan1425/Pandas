# There are diffrent ways of creating DataFrame

# 1st way is from CSV file

import pandas as pd

data = pd.read_csv("C:\\Users\\Sharanm\\Downloads\\stock_prices.csv")
print(pd.DataFrame(data))

print('<--------------------------------------->')
# 2st way is from excel file

data1 = pd.read_excel("C:/Users/Sharanm/Desktop/Testing.xlsx","Sheet1")
print(pd.DataFrame(data1))

print('<--------------------------------------->')

# 3rd way is using python dictionary

details = {'ID':[1,2,3,4,5],
           'First_name':["Sharan","Sai","Vishnu","Raghu","Charan"],
           'Last_name':["Mudiliyar","Singh","Vardhan","Reddy","Kumar"]}
print(pd.DataFrame(details))

print('<--------------------------------------->')

# 4th way is using Tuples list

details1 = [("Benelli", 250000,"Impriale"),
            ("RoyalEnfiled", 210000,"Classic350"),
            ("Halery Dividson", 550000,"BobStreeter")]
print(pd.DataFrame(details1, columns=("Bike_name","Price","Model")))

print('<--------------------------------------->')

#5th way is using dictionary list

car_list = [{'Name':"Audi","Price":"5 Lakhs","Model":"A4"},
            {'Name':"BMW","Price":"10 Lakhs","Model":"Xseries"},
            {'Name':"Porche","Price":"50 Lakhs","Model":"X5"}]
print(pd.DataFrame(car_list))
        