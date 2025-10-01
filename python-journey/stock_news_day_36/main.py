# type: ignore
import os
import requests
import smtplib
from dotenv import load_dotenv
load_dotenv('api.txt')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ALPHAVANTAGE_KEY = os.getenv('ALPHAVANTAGE_KEY')



parameters = {
    "function" : "TIME_SERIES_DAILY" ,
    "symbol" : STOCK ,
    "apikey" : YOUR_ALPHAVANTAGE_KEY
}

stock_data_url = requests.get(STOCK_ENDPOINT ,params=parameters )
stock_data_url.raise_for_status()
stock_data = stock_data_url.json()["Time Series (Daily)"]
data_list = [value for (key , value) in stock_data.items()]
yesterday = float(data_list[0]["4. close"])
before_yesterday = float(data_list[1]["4. close"])

persent = round(((yesterday - before_yesterday) / before_yesterday) * 100 , 2)


if persent > 1 or persent < -1 :
    paramaters = {
    "from" : "2025-06-26",
    "to" : "2025-06-30" ,
    "qInTitle" : COMPANY_NAME ,
    "apiKey" : YOUR_NEWS_API
    }

    data_url = requests.get(NEWS_ENDPOINT, params=paramaters)
    data_url.raise_for_status()
    data = data_url.json()

    for article in data["articles"][:3]:
        description = article["description"]
        title = article["title"]
        message = (f"Headline:\n{title}\n\nBrief:\n{description} \n\n")
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=your_email , password=your_password)
        connection.sendmail(from_addr=your_email , 
                            to_addrs=email_to_send , 
                            msg=f"Subject:TESLA  {persent}\n\n{message}")

