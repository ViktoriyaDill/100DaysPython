import pandas

# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()
# print(max(data_list))
# # average = round(sum(data_list) / len(data_list))
# # print(average)
#
# # average = data["temp"].mean()
# # max_value = data["temp"].max()
# # print(max_value)
#
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp) * 1.8 + 32)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_list = data["Primary Fur Color"].to_list()
new_data = data["Primary Fur Color"].value_counts().to_list()
new_data_key = data["Primary Fur Color"].unique().tolist()
color_dict = {
    "color Fur": new_data_key[1:],
    "Count": new_data
}
df = pandas.DataFrame(color_dict)
df.to_csv("squirrel_count.csv")






