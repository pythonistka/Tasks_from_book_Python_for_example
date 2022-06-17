from tkinter import *
import sqlite3











window = Tk()
window.title("Баллы за тест")
window.geometry("400x150")

enter_lbl = Label(text="Введите имя: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_name = Entry(text="")
enter_name.place(x=150, y=20, width=150, height=25)
enter_name["justify"] = "center"
enter_name.focus()

enter_age_lbl = Label(text="Введите баллы: ")
enter_age_lbl.place(x=50, y=50, width=100, height=25)

enter_age = Entry(text="")
enter_age.place(x=150, y=50, width=150, height=25)
enter_age["justify"] = "center"
enter_age.focus()

add_button = Button(text="Добавить", )
add_button.place(x=150, y=80, width=70, height=25)

show_button = Button(text="Очистить", )
show_button.place(x=230, y=80, width=70, height=25)



window.mainloop()