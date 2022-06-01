from tkinter import *

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
colorList.place(x = 150, y = 60)

window.mainloop()