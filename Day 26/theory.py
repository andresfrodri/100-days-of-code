import random as rd
numbers = [1,2,3,4]

new_list = [n +1 for n in numbers]
print(new_list)

name = 'Salad'
new_list = [letter for letter in name]
print(new_list)

r = range(1,5)

r2=[number*2 for number in r]
print(r2)

names = ['John','Paul','George', 'Ringo','The Beatles'] 

short_names = [name for name in names if len(name)<5]
big_names =  [name.upper() for name in names if len(name)>=5]

print(short_names)
print(big_names)

#Dictionary Comprehension

names = ['John','Paul','George', 'Ringo','The Beatles'] 

scores={musician:rd.randint(90,100) for musician in names}

print(scores)

hall_of_fame ={key: 'Passed' for (key,value) in scores.items() if value>=94}
print(hall_of_fame)