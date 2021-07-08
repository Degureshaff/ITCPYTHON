import json

file = open('books.json','r')
book_json = json.load(file)


print(book_json[0]['title']),
print(book_json[0]['author']),
print(book_json[0]['pages']),
print(book_json[0]['published'])


for i in ['pages'] > 400:
    print(book_json[0]['pages'])
    


