import pandas

data = pandas.read_csv("Section25CSVDataAndPandas\\229DataFrames\weather_data.csv")
# print(type(data))
# prints <class 'pandas.core.frame.DataFrame'>
# print(type(data["temp"]))
# prints <class 'pandas.core.series.Series'>


# data_dict = data.to_dict()
# print(data_dict)


temp_list = data["temp"].to_list()

# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# print(data["temp"].mean())

# print(data["temp"].max())
# print(data.temp)


# print(data[data.day == "Monday"])


# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
def c_to_f(c):
  return c * 9 / 5 + 32

print(c_to_f(monday.temp[0]))




# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Section25CSVDataAndPandas\\229DataFrames\\new_data.csv")