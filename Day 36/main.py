#Stock trading news alert
import json
import datetime as dt
import requests 
import html
import config



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

today=dt.datetime.now().date()
last_friday = (today - dt.timedelta(days=today.weekday()) + dt.timedelta(days=4, weeks=-1))
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
    'apikey': config.api_key,
    'symbol': STOCK,
}

#---------------Get stock values------------------

r1_s=requests.get(url=STOCK_ENDPOINT, params= params_stock)
r1_s.raise_for_status()
stock_data=r1_s.json()
yesterday_close_value = stock_data['Time Series (Daily)'][f'{yesterday}']['4. close']
pre_yesterday_close_value = stock_data['Time Series (Daily)'][f'{before_yes}']['4. close']

diference_perc = (abs(float(yesterday_close_value)-float(pre_yesterday_close_value)))/float(yesterday_close_value) * 100

if diference_perc > 5:
    print('get news')


#-------------------------------Get News of the stocks-----------------------------
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

