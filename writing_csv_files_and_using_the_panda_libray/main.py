import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
        else:
            temperature.append(row[1])
    print(temperature)

import pandas
p_data = pandas.read_csv("weather_data.csv")
print(p_data)
print(p_data["temp"].mean())

# Getting rows from a dataframe. Note that it is done by using conditionals
print(p_data[p_data.temp == p_data.temp.max()])
