# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # my code for average temperature, with Claude's help
# data_frame = pandas.DataFrame(data_dict)
# temp_average = data_frame["temp"].mean()
# print(temp_average)
#
# # solution code for average temperature
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
#
# # my code for max temperature, same as solution code
# print(data["temp"].max())
#
# # get data in columns
# print(data["condition"])
# print(data.condition)
#
# # get data in rows
# print(data[data.day == "Monday"])
#
# # my code for row of data which had the highest temperature, same as solution code
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # my code for retrieving Monday's temperature and converting to Fahrenheit
# print(monday.temp * 9/5 + 32)
#
# # solution code for retrieving Monday's temperature and converting to Fahrenheit
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


# my code for The Great Squirrel Census Data Analysis (with Pandas!), with help from Claude and googling
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_gray_squirrels = squirrel_data["Primary Fur Color"].value_counts()["Gray"]
num_red_squirrels = squirrel_data["Primary Fur Color"].value_counts()["Cinnamon"]
num_black_squirrels = squirrel_data["Primary Fur Color"].value_counts()["Black"]

squirrel_colours_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [num_gray_squirrels, num_red_squirrels, num_black_squirrels]
}

squirrel_count = pandas.DataFrame(squirrel_colours_dict)
print(squirrel_count)
squirrel_count.to_csv("squirrel_count.csv")

# solution code for The Great Squirrel Census Data Analysis (with Pandas!)
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_solution.csv")