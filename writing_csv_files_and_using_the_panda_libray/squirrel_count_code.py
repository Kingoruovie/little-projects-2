import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

dict_of_squirrel_class_by_color = {"Fur Color": ["Gray", "Red", "Black"], "Count": [gray, red, black] }
squirrel_data_table = pd.DataFrame(dict_of_squirrel_class_by_color)
squirrel_data_table.to_csv("Squirrel_color_count.csv")