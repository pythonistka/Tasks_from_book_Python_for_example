from tkinter import *

def add_on():
    name = enter_name.get()
    output_names.insert(END, name)
    enter_name.delete(0, END)
    enter_name.focus()

def reset():
    output_names.delete(0, END)
    enter_name.focus()


window = Tk()
window.title("Список имен")
window.geometry("450x180")

enter_lbl = Label(text="Введите имя: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_name = Entry(text=0)
enter_name.place(x=150, y=20, width=100, height=25)
enter_name["justify"] = "center"
enter_name.focus()

add_button = Button(text="Добавить", command=add_on)
add_button.place(x=300, y=20, width=80, height=25)

output_lbl = Label(text="Список:")
output_lbl.place(x=50, y=50, width=100, height=25)

output_names = Listbox()
output_names.place(x=150, y=50, width=100, height=100)
output_names["bg"] = "white"
output_names["relief"] = "sunken"
output_names["justify"] = "center"

button_clear = Button(text="Очистить", command=reset)
button_clear.place(x=300, y=50, width=80, height=25)

window.mainloop()