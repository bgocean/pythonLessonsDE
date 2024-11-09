import requests
import pandas as pd

api_key = '1bbd0e4feae573037172783bf5a5ac2b'
curr = 'UAH,GBP,EUR'
start_date = '2013-11-09'
end_date = '2013-11-09'
URL = f'http://api.currencylayer.com/change?access_key={api_key}&currencies={curr}&start_date={start_date}&end_date={end_date}'

r = requests.get(url=URL)
result = r.json()

data = []
date = start_date

# Создаем данные для DataFrame
for currency, rate in result.get('quotes', {}).items():
    data.append([date, currency[3:], rate])

# Создаем DataFrame и записываем в CSV
df = pd.DataFrame(data, columns=['Дата', 'Валюта', 'Курс к доллару'])
df.to_csv('exchange_rates2.csv', index=False)
