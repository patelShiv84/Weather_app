import requests
from config import API_KEY, BASE_URL

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code != 200:
            print("Please enter a valid city name.")
            return None

        
        city = data['name']
        temperature = data['main']['temp']
        condition = data['weather'][0]['description']  # <----- 

        
        return {
            'location': city,
            'temperature': temperature,
            'condition': condition
        }

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

# if __name__ == "__main__":
#     city_name = "Surat"
#     result = get_weather_data(city_name)
#     print(result)
