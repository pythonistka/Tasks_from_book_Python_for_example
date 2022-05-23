from tkinter import *

def add_on_mile():
    num = enter_num.get()
    num = int(num)
    mile = num * 0.6214
    output_num["text"] = mile

def add_on_km():
    num = enter_num.get()
    num = int(num)
    km = num * 1.6093
    output_num["text"] = km


window = Tk()
window.title("Расчет дистанции")
window.geometry("450x100")

enter_lbl = Label(text="Введите длину: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_num = Entry(text=0)
enter_num.place(x=150, y=20, width=100, height=25)
enter_num["justify"] = "center"
enter_num.focus()

mile_button = Button(text="Расчет в милях", command=add_on_mile)
mile_button.place(x=300, y=20, width=120, height=25)

km_button = Button(text="Расчет в км", command=add_on_km)
km_button.place(x=300, y=50, width=120, height=25)

output_lbl = Label(text="Результат:")
output_lbl.place(x=50, y=50, width=100, height=25)

output_num = Message(text=0)
output_num.place(x=150, y=50, width=100, height=25)
output_num["bg"] = "white"
output_num["relief"] = "sunken"
output_num["justify"] = "center"

window.mainloop()