#Stock trading news alert
import datetime as dt
import requests 
from twilio.rest import Client
import config



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token


today=dt.datetime.now().date()
last_friday = (today - dt.timedelta(days=today.weekday()) + dt.timedelta(days=4, weeks=-1))
week_before =(today - dt.timedelta(days=today.weekday()) + dt.timedelta(days=4, weeks=-1))
if today.weekday()>5:
    yesterday=last_friday
else:
    yesterday=today-dt.timedelta(1)

if yesterday.weekday() == 0:
    before_yes=last_friday
else:
    before_yes=yesterday-dt.timedelta(1)

params_stock={
    'function':'TIME_SERIES_DAILY',
    'apikey': config.api_key_stock,
    'symbol': STOCK,
}

params_news ={
    'apiKey': config.api_key_news,
    'q': COMPANY_NAME,
    'from':week_before,
    'to':today,
    'pageSize':3,
}
#---------------Get stock values------------------

r1_s=requests.get(url=STOCK_ENDPOINT, params= params_stock)
r1_s.raise_for_status()
stock_data=r1_s.json()
yesterday_close_value = stock_data['Time Series (Daily)'][f'{yesterday}']['4. close']
pre_yesterday_close_value = stock_data['Time Series (Daily)'][f'{before_yes}']['4. close']

diference_perc = round((float(yesterday_close_value)-float(pre_yesterday_close_value)))/float(yesterday_close_value * 100,2)

if diference_perc > 5:
    #-------------------------------Get News of the stocks-----------------------------
    r2_n=requests.get(url=NEWS_ENDPOINT, params=params_news)
    r2_n.raise_for_status()
    news_data = r2_n.json()
    news_list = news_data['articles']
    client = Client(account_sid, auth_token)
    for i in range(len(news_list)):
        title=news_data['articles'][i]['title']
        brief = news_data['articles'][i]['description']
        text=f'{STOCK} moved {diference_perc}%\nHeadline: {title}\nBrief: {brief}'
        message = client.messages \
                .create(
                     body=text,
                     from_=config.twilio_phone_num,
                     to= config.my_phone_num
                 )
        print(message.status)
