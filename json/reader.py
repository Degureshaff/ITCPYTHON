import json

user = {        
    "name": "Нурбек",
    "age": 26,
    "birthDate": "02.06.2021",
    "city": "Osh"
    }


user_json = open('users.json','w')
# записать в dict в файл
user_dict = json.dump(user,user_json)

user_json = open('users.json','r')
# прочитать json в файл
user_dict = json.load(user_json)
print(user_dict)








