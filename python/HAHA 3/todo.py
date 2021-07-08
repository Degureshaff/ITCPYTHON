import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.117",
  user="group2",
  password="1",
  database = 'itc_group_2',
)

tododb = mydb.cursor()


while True:
    todo = input('введите задачу: ')
    sql = "INSERT INTO todo(todo) VALUES('{}')".format(todo)
    val = (todo)
    tododb.execute(sql,val)
    tododb.commit()


    if todo == 'exit':
        break

    print(sql)