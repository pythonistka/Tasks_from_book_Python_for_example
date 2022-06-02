from tkinter import *

def add_to_list():
    name = enter_name.get()
    sex = selectSex.get()
    name_sex = name + ", " + sex
    show_section.insert(END, name_sex)
    enter_name.delete(0, END)
    selectSex.set("Ваш пол")


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


window.mainloop()