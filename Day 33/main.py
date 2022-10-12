import requests
import datetime as dt
import smtplib
import time 

email='###########@gmail.com'
password='##################'

my_lat = 5.538590
my_lng= -73.366379
my_tup=(my_lat, my_lng)



def iss_pos_checker():
    response=requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    if my_lng - 5<=longitude <= my_lng + 5  and  my_lat - 5 <= latitude <=my_lat + 5:      
        return True
    else:
        return False

def is_night():
    parameters={
        'lat': my_lat,
        'lng': my_lng,
        'formatted':0,
    }

    response2 = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response2.raise_for_status()
    data=response2.json()
    sunrise=int(data['results']['sunrise'].split('T')[1].split(':')[0])-5
    sunset=int(data['results']['sunset'].split('T')[1].split(':')[0])-5
    now = dt.datetime.now()
    now_hour=now.hour
    if now_hour>=sunset or now_hour<=sunrise:
        return True
while True:
    time.sleep(60)
    if iss_pos_checker() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email, to_addrs=email,
            msg='Subject:Look up! \n \n The ISS is in top of you!'
        )