# with open("Section25CSVDataAndPandas\\228ReadingCSVData\weather_data.csv") as data_file:
#     print(data_file.readlines())
    
    
# import csv
# with open("Section25CSVDataAndPandas\\228ReadingCSVData\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)



import pandas

data = pandas.read_csv("Section25CSVDataAndPandas\\228ReadingCSVData\weather_data.csv")
print(data["temp"])

