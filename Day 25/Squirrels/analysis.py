import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

squirrel_color = data['Primary Fur Color']

#print(squirrel_color.head())

data_to_export = squirrel_color.value_counts()

data_to_export.to_csv('squirrel_count.csv')


