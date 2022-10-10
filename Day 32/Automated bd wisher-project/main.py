
import smtplib
import pandas as pd
import datetime as dt
import random as rd

now=dt.datetime.now()
today=(now.month,now.day)

my_email = '######@gmail.com'
password='######################'

birth_day_df=pd.read_csv(r'Day 32\Automated bd wisher-project\birthdays.csv')

birth_day_dict = {(row['month'], row['day']):row for (index,row) in birth_day_df.iterrows()}

for i in birth_day_dict:
    if i == today:
        with open(f'Day 32\Automated bd wisher-project\letter_templates\letter_{rd.randint(1,3)}.txt') as file:
            bd_person=birth_day_dict[i]
            message=file.read()
            message = message.replace('[NAME]',f'{bd_person["name"]}')

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=bd_person['email'],
    msg=f'Subject: Birthday message \n\n{message}')