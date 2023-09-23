import requests
import subprocess
from PIL import Image
from io import BytesIO



def photo_search(api_key: str, url: str):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data['urls']['regular']
    else:
        print('Failed to receive data from server')
        return None

    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image.save(f'{query}.jpg')
        print('Image saved successfully')
    else:
        print("Image didn't find")
        return None

    try:
        subprocess.run(['start', f'{query}.jpg'], shell=True)
    except Exception as e:
        print(f'Error opening the image: {e}')


api_key = 'Rsz6NG9nFf8ioprDLBo7GTuCu6dQX5WeiXlVuB3hCX0'
query = input('Enter your keyword: ')
url = f'https://api.unsplash.com/photos/random/?query={query}&client_id={api_key}'

photo_search(api_key, url)
