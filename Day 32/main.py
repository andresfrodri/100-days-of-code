
import smtplib
import datetime as dt
import random as rd

now=dt.datetime.now()
year=now.year
day=now.weekday()

my_email = '#########@gmail.com'
password='#####################'

if day == 6:
    with open('Day 32\quotes.txt','r') as file:
        lines=file.readlines()
        text=rd.choice(lines)
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs='######@gmail.com',
            msg=f'Subject:Hello, this is a motivational quote! \n\n {text}.')