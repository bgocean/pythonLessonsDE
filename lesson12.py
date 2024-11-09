import csv

import requests

# URL = f"https://randomuser.me/api/"
# https://catfact.ninja/fact
# https://randomuser.me/api/
# https://dog.ceo/api/breeds/image/random

# r = requests.get(url=URL)
# result = r.json()
#
# if r.status_code == 200:
#     print(result)
#     print(type(result))
#     print(r.text)
#     print(r.status_code)
# else:
#     print('was error')
#     print(r.status_code)
#     print(r.text)

api_key = '1bbd0e4feae573037172783bf5a5ac2b'
curr = 'UAH,GBP,EUR'
start_date = '2013-11-09'
end_date = '2013-11-09'
URL = f'http://api.currencylayer.com/change?access_key={api_key}&currencies={curr}&start_date={start_date}&end_date={end_date}'
r = requests.get(url=URL)
result = r.json()
print(result)
# print(result.get('quotes').get('USDUAH'))
# print(result.get('quotes').get('USDGBP'))
# print(result.get('quotes').get('USDEUR'))
# Создаем и записываем в CSV файл
with open('currency_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Currency', 'Change'])

    quotes = result.get('quotes', {})
    for currency, change in quotes.items():
        writer.writerow([currency, change])