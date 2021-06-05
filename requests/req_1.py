import requests

api_key = 'fa0c69065a227aae0ae1081d5953bcfa'
site = 'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=metric'

city = input('введите ваш город: ').title()
state = input('введите код страны: ').upper()

site = site.format(city = city,state = state,api_key = api_key)



data = requests.get(site)
data_dict = data.json()

print('погода в', city)
print(data_dict['main']['temp'], 'градус')
print(data_dict['main']['feels_like'], 'ошушается')
print(data_dict['weather'][0]['main'], 'облачно')
