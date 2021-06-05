import json

file = open('countries1.json','r')
countries = json.load(file)

while True:
    name = input('введите имя страны: ')
    
    if name == 'exit':
        break
    for country in countries:
        if country['country'] == name:
            print(country['calling_code'])

