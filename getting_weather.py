import requests
from pprint import pprint

API_key = '95be7ffdc46fe199c31e94814842e550'

city = input('Enter city: ')

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + API_key

weather_data = requests.get(url).json()

pprint(weather_data)