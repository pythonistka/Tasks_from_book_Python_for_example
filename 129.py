from tkinter import *


def add_num():
    num = enter_num.get()
    if num.isdigit():
        output_nums.insert(END, num)
        enter_num.delete(0, END)
        enter_num.focus()


def reset():
    output_nums.delete(0, END)
    enter_num.focus()


window = Tk()
window.title("Список чисел")
window.geometry("450x200")

enter_lbl = Label(text="Введите число: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_num = Entry(text=0)
enter_num.place(x=150, y=20, width=100, height=25)
enter_num["justify"] = "center"
enter_num.focus()

add_button = Button(text="Добавить", command=add_num)
add_button.place(x=300, y=20, width=120, height=25)

output_nums = Listbox()
output_nums.place(x=150, y=50, width=100, height=100)
output_nums["bg"] = "white"
output_nums["relief"] = "sunken"
output_nums["justify"] = "center"

button_clear = Button(text="Очистить", command=reset)
button_clear.place(x=300, y=50, width=120, height=25)

window.mainloop()
