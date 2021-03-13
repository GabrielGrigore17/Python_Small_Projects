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

# import pandas


# def f(x):
#     x = x * 1.8 + 32
#     return float(x)
#
#
# data = pandas.read_csv("weather_data.csv")
# # temperatures = data["temp"].to_list()
# # print(sum(temperatures)/len(temperatures))
# # print(data["temp"].max())
# # print(data[data.temp == data.temp.max()])
# # print(f(data[data.day == "Monday"].temp))
# print(data.to_dict())

import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colours = data["Primary Fur Color"].to_list()
cleaned_colours = [x for x in colours if str(x) != 'nan']
data_dict = {i: cleaned_colours.count(i) for i in cleaned_colours}
final_data_dict = {
    "Colour": list(data_dict.keys()),
    "No": list(data_dict.values())
}
data_output = pandas.DataFrame(final_data_dict)
data_output.to_csv("data_output.csv")
