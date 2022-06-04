from tkinter import *

def add_to_list():
    file = open("Names_and_sex.csv", "a")
    name = enter_name.get()
    sex = selectSex.get()
    name_sex = name + ", " + sex + "\n"
    file.write(str(name_sex))
    file.close()
    enter_name.delete(0, END)
    selectSex.set("Ваш пол")


def show_list():
    file = open("Names_and_sex.csv", "r")
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        show_section.insert(END, data)
        x = x + 1


window = Tk()
window.title("Список имён")
window.geometry("450x200")

enter_lbl = Label(text="Введите имя: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_name = Entry(text="")
enter_name.place(x=150, y=20, width=100, height=25)
enter_name["justify"] = "center"
enter_name.focus()

selectSex = StringVar(window)
selectSex.set("Ваш пол")
colorList = OptionMenu(window, selectSex, "Женский", "Мужской")
colorList.place(x = 280, y = 17)

add_button = Button(text="Добавить", command=add_to_list)
add_button.place(x=150, y=60, width=100, height=25)

show_lbl = Label(text="Cписок: ")
show_lbl.place(x=50, y=95, width=100, height=25)

show_section = Listbox()
show_section.place(x=150, y=100, width=100, height=70)
show_section["justify"] = "center"
show_section.focus()

show_button = Button(text="Вывести", command=show_list)
show_button.place(x=280, y=100, width=90, height=25)


window.mainloop()