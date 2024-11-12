# подключаем библиотеку для работы с запросами


import requests
# указываем город
city = 'Киев'
# формируем запрос
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url).json()
print(weather_data)
# получаем данные о температуре и о том, как она ощущается
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
# выводим значения на экран
print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')

print('==========================================================')

import json
from datetime import datetime

# Данные JSON
data = {
    'coord': {'lon': 30.5167, 'lat': 50.4333},
    'weather': [{'id': 801, 'main': 'Clouds', 'description': 'небольшая облачность', 'icon': '02d'}],
    'base': 'stations',
    'main': {
        'temp': 4.98, 'feels_like': 4.98, 'temp_min': 4.84, 'temp_max': 7.54,
        'pressure': 1033, 'humidity': 79, 'sea_level': 1033, 'grnd_level': 1016
    },
    'visibility': 10000,
    'wind': {'speed': 0.45, 'deg': 240, 'gust': 1.79},
    'clouds': {'all': 11},
    'dt': 1731408690,
    'sys': {'country': 'UA', 'sunrise': 1731388059, 'sunset': 1731421004},
    'timezone': 7200,
    'id': 703448,
    'name': 'Киев',
    'cod': 200
}

# Функция для форматирования времени
def format_timestamp(timestamp, timezone):
    dt = datetime.utcfromtimestamp(timestamp + timezone)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

# Расшифровка JSON
city_name = data.get('name', 'Unknown')
country = data['sys'].get('country', 'Unknown')
longitude = data['coord'].get('lon', 0)
latitude = data['coord'].get('lat', 0)

# Погода
weather_description = data['weather'][0].get('description', 'No description')
weather_main = data['weather'][0].get('main', 'Unknown')
icon = data['weather'][0].get('icon', '')

# Температура и давление
temp = data['main'].get('temp', 0)
feels_like = data['main'].get('feels_like', 0)
temp_min = data['main'].get('temp_min', 0)
temp_max = data['main'].get('temp_max', 0)
pressure_hpa = data['main'].get('pressure', 0)
pressure_mmHg = round(pressure_hpa * 0.75006, 2)
humidity = data['main'].get('humidity', 0)

# Ветер
wind_speed = data['wind'].get('speed', 0)
wind_deg = data['wind'].get('deg', 0)
wind_gust = data['wind'].get('gust', 0)

# Облачность
cloudiness = data['clouds'].get('all', 0)

# Видимость
visibility = data.get('visibility', 0)

# Время восхода и заката
sunrise = format_timestamp(data['sys'].get('sunrise', 0), data.get('timezone', 0))
sunset = format_timestamp(data['sys'].get('sunset', 0), data.get('timezone', 0))

# Время обновления данных
dt = format_timestamp(data.get('dt', 0), data.get('timezone', 0))

# Вывод данных
print(f"Город: {city_name}, Страна: {country}")
print(f"Координаты: долгота {longitude}, широта {latitude}")
# print(f"Погода: {weather_main} ({weather_description}), Иконка: {icon}")
print(f"Погода: {weather_main} ({weather_description})")
print(f"Температура: {temp}°C, Ощущается как: {feels_like}°C")
print(f"Минимальная температура: {temp_min}°C, Максимальная температура: {temp_max}°C")
print(f"Давление: {pressure_mmHg} мм рт. ст., Влажность: {humidity}%")
print(f"Скорость ветра: {wind_speed} м/с, Направление: {wind_deg}°, Порывы: {wind_gust} м/с")
print(f"Облачность: {cloudiness}%")
print(f"Видимость: {visibility} м")
print(f"Восход солнца: {sunrise}, Закат солнца: {sunset}")
print(f"Обновление данных: {dt}")
