# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdecimal():
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# temperatures = data["temp"].to_list()
# print(sum(temperatures)/len(temperatures))
print(data["temp"].max())
print(data[data.temp == data.temp.max()])
