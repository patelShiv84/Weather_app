import requests
from config import API_KEY, BASE_URL

city = "Surat"

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)  
else:
    print("Failed to fetch weather data")
