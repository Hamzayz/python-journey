with open("day 25/weather_data.csv") as data_file:
    data = data_file.readlines()
    for row in data:
        print(row)

import csv
import pandas

with open("day 25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if len(row) > 1:  # Skip empty rows
            try:
                temp = int(row[1])  # Convert temperature to integer
                temperature.append(temp)
            except ValueError:
                continue  # Skip header row or invalid data
    
    print(temperature)  # Print the final list of temperatures

data = pandas.read_csv("day 25/weather_data.csv")
print(type(data))
print(data["temp"]) 

# pandas have two data types :
# series : Is a data type that contains coloms 
# DataFrame : A DataFrame is a 2-dimensional labeled data structure in pandas, similar 
# to a spreadsheet or SQL table.

data_dict = data.to_dict() # it will convert data in to dictionary type
# print(data_dict)
    
temperature = data["temp"].to_list()
sum = sum(temperature)

# Calculate average by dividing total by number of temperatures
average = sum / len(temperature)
print(f"Average temperature: {average}")
# finding average by pandas :
print(data["temp"].mean())
max = data["temp"].max()

row = (data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temper = monday.temp
print(temper)
fahrenheit=(temper * 9/5) + 32
print(fahrenheit)

datas = pandas.read_csv("day 25/Central_Park_Squirrel.csv")
no_Gray = len(datas[datas["Primary Fur Color"] == "Gray"])
no_black = len(datas[datas["Primary Fur Color"] == "Black"])
no_cinnamon = len(datas[datas["Primary Fur Color"] == "Cinnamon"])

print(no_Gray)
print(no_black)
print(no_cinnamon)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [no_Gray, no_black, no_cinnamon]
}

df = pandas.DataFrame(data_dict)
df.to_csv("day 25/squiral_count.csv")
