#to download files with python use request
import requests
#to change time entered into epoc time
from datetime import datetime
#for time convergence
import time

#Collecting data from yahoo finance
#collect user input for date
ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

#formatting date time to epoch
from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


yahoofinance = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
#Due to security on page we will need to add headers to access page so the script to run
yahfinheaders = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
#using requests to create variable stock_content by requesting the download from the site
##created yahfinheaders variable to get method to add in script running on secure page
stock_content = requests.get(yahoofinance, headers=yahfinheaders).content

#create a file
with open('yahfindoc.csv', 'wb') as file:
    file.write(stock_content)
