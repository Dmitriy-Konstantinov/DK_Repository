import requests


def get_weather(api_key: str, city: str):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}')

    if response.status_code == 200:
        data = response.json()
        current_temperature = round(data['main']['temp'] - 273.15)
        print(f'Current temperature in {city} is {current_temperature}°C')
    else:
        print('Failed to receive data from server')


api_key = '59740aba4237aa12248907241c870d08'
city = 'Kyiv'

get_weather(api_key, city)
