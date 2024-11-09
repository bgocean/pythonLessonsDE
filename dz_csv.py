import requests
import csv
from datetime import datetime

api_key = '1bbd0e4feae573037172783bf5a5ac2b'
curr = 'UAH,GBP,EUR'
start_date = '2013-11-09'
end_date = '2013-11-09'
URL = f'http://api.currencylayer.com/change?access_key={api_key}&currencies={curr}&start_date={start_date}&end_date={end_date}'

r = requests.get(url=URL)
result = r.json()

# Открываем файл для записи
with open('exchange_rates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Дата', 'Валюта', 'Курс к доллару'])

    date = start_date  # Используем дату из запроса
    for currency, rate in result.get('quotes', {}).items():
        writer.writerow([date, currency[3:], rate])
