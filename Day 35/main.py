import requests
from twilio.rest import Client
import config


lati, long = 5.532303, -73.361793
a_api_key = config.OWM_api_key
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token


w_params= {
            'lat':lati,
            'lon':long,
            'exclude':'current,minutely,daily' ,
            'appid':a_api_key,
}

response = requests.get(OWM_Endpoint,params=w_params)
response.raise_for_status()

full_w_data=response.json()

h_w_data = full_w_data['hourly']

def will_rain():
    for i in h_w_data[:12]:
        a=int(i["weather"][0]["id"])
        if a<700:
            return True
        else:
            print('It will not rain!')
            return False


a=will_rain()

if a:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body='It will rain! \nBring an umbrella 😅',
                     from_=config.twilio_phone_num,
                     to= config.my_phone_num
                 )
    print(message.status)
