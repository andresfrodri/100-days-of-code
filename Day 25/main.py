path = r'Day 25\weather_data.csv'
#with open(path, 'r') as data_file:
#    data_list = data_file.readlines()
#print(data_list)

#The way above was awful to use

#import  csv

#with open(path, 'r') as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for i in data:
#        if i[1] != 'temp':
#            temperatures.append(int(i[1]))




#print(temperatures)

import pandas as pd

data=pd.read_csv(path)
print(data)
print(data['temp'])

temp_list=data['temp'].to_list()

print(temp_list)

print(data[data.temp == data['temp'].max()])

monday = data[data.day == 'Monday']

print(monday.condition)