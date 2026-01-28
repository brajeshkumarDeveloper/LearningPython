# acb18926a7082d0bbe0de6f8d0d9fd32
import requests

API_KEY='acb18926a7082d0bbe0de6f8d0d9fd32'
city_name=input('Enter city name: ')
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
response = requests.get(url)
# print(response)
# print(response.json())
if response.status_code == 200:
    weather_data = response.json()
    weather_desc = weather_data['weather'][0]['description']
    temp=weather_data['main']['temp']
    temp_celcius=temp-273.15
    print(f'Weather in {city_name}: {round(temp_celcius,2)} C with {weather_desc}')
else :
    print(f'City name {city_name} not found or incorrect')