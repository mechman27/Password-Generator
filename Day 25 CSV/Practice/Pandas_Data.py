# import csv

# with open('Intermediate/Day 25/weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row [1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)
import pandas as pd

data = pd.read_csv('Intermediate/Day 25/weather_data.csv')
print(data["temp"])

print(data["temp"].mean())
print(data["temp"].max())

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)


print(f"{monday_temp*(9/5)+32}F")

##################################################
#Creating a Dataframe
data_dict = {
    "students": ["John", "Angela", "David"], 
    "grades": [100, 90, 80]
    }
dict_data = pd.DataFrame(data_dict)

dict_data.to_csv("Intermediate/Day 25/new_data.csv")