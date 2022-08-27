from tkinter import *


def add_on():
    num = enter_txt.get()
    num = int(num)
    for i in range(1, 11):
        mult = i * num
        output_txt.insert(END, (i, "*", num, "=", mult))
    enter_txt.delete(0, END)
    enter_txt.focus()


def clear():
    enter_txt.delete(0, END)
    output_txt.delete(0, END)
    enter_txt.focus()


total = 0
num = 0
window = Tk()
window.title("Таблица умножения")
window.geometry("500x250")

enter_lbl = Label(text="Введите число: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_txt = Entry(text=0)
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt["justify"] = "center"
enter_txt.focus()

add_button = Button(text="Таблица умножения", command=add_on)
add_button.place(x=300, y=20, width=150, height=25)

output_lbl = Label(text="Ответ:")
output_lbl.place(x=50, y=50, width=100, height=25)

output_txt = Listbox()
output_txt.place(x=150, y=50, width=100, height=180)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

button_clear = Button(text="Очистка", command=clear)
button_clear.place(x=300, y=50, width=150, height=25)

window.mainloop()
