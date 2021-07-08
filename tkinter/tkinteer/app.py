from tkinter import * 
from tkinter import messagebox 
import sqlite3 

db = sqlite3.connect('./db.sqlite3')

dbcursor = db.cursor()
dbcursor.execute('SELECT * FROM settings')

settings = dbcursor.fetchall()

for config in settings:
    if config[1] == 'title': 
        app_title = config[2]
    elif config[1] == 'message':
        ms = config[2]
    elif config[1] == 'size':
        r = config[2]
    elif config[1] == 't':
        t = config[2]
    elif config[1] == 'z':
        z = config[2]





def clicked():  
    messagebox.showinfo(z, t) 

app = Tk()  
app.title(app_title)
# текст в окне
flabel = Label(app, text = ms, font = ('colibti', 24))
# размер окна app
app.geometry(r)
# кординаты окна
flabel.grid(column=0, row=0)  
# кнопка
btn = Button(app, text='', command=clicked)  
btn.grid(column=1, row=0) 


app.mainloop()