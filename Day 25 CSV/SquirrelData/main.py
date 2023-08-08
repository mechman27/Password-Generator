import pandas as pd

data = pd.read_csv('Intermediate/Day 25/SquirrelData/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey = len(data["Primary Fur Color"] == "Grey")
cinnamon = len(data["Primary Fur Color"] == "Cinnamon")
black = len(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey, cinnamon, black]
}

df = pd.DataFrame(data_dict)
df.to_csv('Intermediate/Day 25/SquirrelData/Squirrel_Count.csv')
