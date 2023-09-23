import requests
import json


def get_url_api(url):
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        print('Failed to receive data from server')


url = 'https://api.openweathermap.org/data/2.5/weather?q=London&APPID=59740aba4237aa12248907241c870d08'
json_file = get_url_api(url)
print(json.dumps(json_file, indent=4))
