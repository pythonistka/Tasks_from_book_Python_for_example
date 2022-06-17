from tkinter import *
import sqlite3

def add_name():
    name = enter_name.get()
    score = enter_score.get()

    cursor.execute("""INSERT INTO namesandscores(name, score)
     VALUES(?,?)""", (name, score))
    db.commit()

    enter_name.delete(0, END)
    enter_score.delete(0, END)
    enter_name.focus()


def clear_window():
    enter_name.delete(0, END)
    enter_score.delete(0, END)
    enter_name.focus()


with sqlite3.connect("testscores.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS namesandscores(
 id integer PRIMARY KEY,
 name text NOT NULL,
 score integer);""")


window = Tk()
window.title("Баллы за тест")
window.geometry("400x150")

enter_lbl = Label(text="Введите имя: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_name = Entry(text="")
enter_name.place(x=150, y=20, width=150, height=25)
enter_name["justify"] = "center"
enter_name.focus()

enter_score_lbl = Label(text="Введите баллы: ")
enter_score_lbl.place(x=50, y=50, width=100, height=25)

enter_score = Entry(text="")
enter_score.place(x=150, y=50, width=150, height=25)
enter_score["justify"] = "center"
enter_score.focus()

add_button = Button(text="Добавить", command=add_name)
add_button.place(x=150, y=80, width=70, height=25)

show_button = Button(text="Очистить", command=clear_window)
show_button.place(x=230, y=80, width=70, height=25)

cursor.execute("SELECT * FROM namesandscores")
for x in cursor.fetchall():
    print(x)


window.mainloop()
db.close()



