import requests
import json


def converter(api_key: str, url: str, converted_currency: str, amount: float):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        result = round(data['conversion_rates'][converted_currency] * amount, 2)
        return result
    else:
        print('Failed to receive data from server')


api_key = '4d07aa06a1d532e8361d2a0c'
base_currency = input('Enter currency to convert: ').upper()
amount = float(input(f'Enter amount of {base_currency}: '))
converted_currency = input('Enter the currency to be converted to: ').upper()
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'

print(converter(api_key, url, converted_currency, amount))
