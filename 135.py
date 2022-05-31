from tkinter import *

def add_color():
    sel = selectColor.get()
    if sel == "Красный":
        window.configure(background="red")
    elif sel == "Жёлтый":
        window.configure(background="yellow")
    elif sel == "Голубой":
        window.configure(background="blue")
    elif sel == "Розовый":
        window.configure(background="pink")


window = Tk()
window.configure(background = "black")
window.title("Выбор цвета")
window.geometry("300x150")

selectColor = StringVar(window)
selectColor.set("Выбери цвет")
colorList = OptionMenu(window, selectColor, "Красный", "Жёлтый", "Голубой", "Розовый")
colorList.place(x = 30, y = 30)

add_button = Button(text="Выбрать", command=add_color)
add_button.place(x=180, y=35, width=80, height=25)

window.mainloop()