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

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# my code for average temperature, with Claude's help
data_frame = pandas.DataFrame(data_dict)
temp_average = data_frame["temp"].mean()
print(temp_average)

# solution code for average temperature
average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())

# my code for max temperature, same as solution code
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in rows
print(data[data.day == "Monday"])

# my code for row of data which had the highest temperature, same as solution code
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# my code for retrieving Monday's temperature and converting to Fahrenheit
print(monday.temp * 9/5 + 32)

# solution code for retrieving Monday's temperature and converting to Fahrenheit
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")