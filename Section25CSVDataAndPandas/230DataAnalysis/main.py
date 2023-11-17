import pandas


squirrel_data = pandas.read_csv("Section25CSVDataAndPandas\\230DataAnalysis\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")



data_dict = {
    "squirrel_color": ["Gray", "Black", "Cinnamon"],
    "scores": [len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]), len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]), len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Section25CSVDataAndPandas\\230DataAnalysis\\new_data.csv")
    