import json



person = {}

login = input('введите логин: ')
name = input('введите имя: ')

person['login'] = login
person['name'] = name

person_json = open('person_json','w')
json.dump(person, person_json)

print(person)


