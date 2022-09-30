weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday':18,
    'Thursday':20,
    'Friday' : 15,
    'Saturday' : 18,
    'Sunday' : 21,
}

weather_f =  {key : (value*9/5)+32 for (key,value) in weather_c.items()}
print(weather_f)