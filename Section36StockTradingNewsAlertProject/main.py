from decouple import config
import requests


alpha_vantage_api_key = config("alpha_vantage_api_key")
news_api_key = config("news_api_key")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def get_news():
    news_parameters = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "pageSize": 1
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters) 
    news_response.raise_for_status()
    news_data = news_response.json()
    for article in news_data["articles"]:
        print(article["author"])
        print(article["title"])
        print(article["description"])

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "apikey": alpha_vantage_api_key,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY"
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters) 
stock_response.raise_for_status()
stock_data = stock_response.json()
daily_stock_data = stock_data["Time Series (Daily)"]
daily_stock_list = [value for (key, value) in daily_stock_data.items()]
yesterday_stock_data = daily_stock_list[0]
two_days_ago_stock_data = yesterday_stock_data[1]

if float(yesterday_stock_data['4. close']) > float(two_days_ago_stock_data['4. close']) * 1.05 or float(yesterday_stock_data['4. close']) < float(two_days_ago_stock_data['4. close']) * .95:
    get_news()






    
    
    
#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
