# import csv
#
# with open("weather_data.csv") as weather_csv:
#     data = csv.reader(weather_csv)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# num_of_temp = len(temp_list)
# avg_temp = sum(temp_list) / num_of_temp
# print(round(avg_temp))
#
# print(data[data.temp == data.temp.max()])

# Get data in row
monday = data[data.day == "Monday"]
cel = int(monday.temp)
fah = (cel * 1.8) + 32
print(fah)


# Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data_1 = pandas.DataFrame(data_dict)
data_1.to_csv("new_student.csv")

