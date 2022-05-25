import csv
from tkinter import *

def show_file():
    file = open("Names_and_ages.csv", "r")
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        show_section.insert(END, data)
        x = x + 1


def add_to_file():
    file = open("Names_and_ages.csv", "a")
    name = enter_name.get()
    age = enter_age.get()
    new_rec = name + ", " + age + "\n"
    file.write(str(new_rec))
    file.close()
    enter_name.delete(0, END)
    enter_age.delete(0, END)


window = Tk()
window.title("Список имён")
window.geometry("450x200")

enter_lbl = Label(text="Введите имя: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_name = Entry(text="")
enter_name.place(x=150, y=20, width=100, height=25)
enter_name["justify"] = "center"
enter_name.focus()

enter_age_lbl = Label(text="Введите возраст: ")
enter_age_lbl.place(x=50, y=50, width=100, height=25)

enter_age = Entry(text="")
enter_age.place(x=150, y=50, width=100, height=25)
enter_age["justify"] = "center"
enter_age.focus()

add_button = Button(text="Добавить", command=add_to_file)
add_button.place(x=300, y=20, width=120, height=25)

show_lbl = Label(text="Вывести список: ")
show_lbl.place(x=50, y=80, width=100, height=25)

show_section = Listbox()
show_section.place(x=150, y=80, width=100, height=100)
show_section["justify"] = "center"
show_section.focus()

show_button = Button(text="Вывести", command=show_file)
show_button.place(x=300, y=80, width=120, height=25)

window.mainloop()
