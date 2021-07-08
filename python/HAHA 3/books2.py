import mysql.connector
import json


mydb = mysql.connector.connect(
  host="192.168.0.117",
  user="group2",
  password="1",
  database = 'itc_group_2',
)

booksdb = mydb.cursor()

file = open('books.json', 'r')

books = json.load(file)

for book in books:
    sql = '''
        INSERT INTO 
            books(
                isbn, 
                title, 
                subtitle, 
                author,
                publisher,
                pages,
                website
            ) VALUES(
                "{}", 
                "{}", 
                "{}", 
                "{}", 
                "{}",
                 {},
                "{}"
            )
    '''.format(
        book['isbn'], 
        book['title'], 
        book['subtitle'], 
        book['author'],
        book['publisher'],
        book['pages'],
        book['website']
    )
    booksdb.execute(sql)
    print(sql)
mydb.commit()




