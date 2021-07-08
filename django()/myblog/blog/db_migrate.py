from .db import mydb

cur = mydb.cursor()


cur.execute('''
INSERT INTO todos(todo_name) 
VALUES
    ("Play football"),
    ("Learn python"),
    ("приготовить еду"),
    ("починить дверь");
''')

mydb.commit()

