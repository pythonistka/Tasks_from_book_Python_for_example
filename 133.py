from tkinter import *


def click():
    name = textbox1.get()
    message = str("Привет" + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2["text"] = message


window = Tk()
window.wm_iconbitmap("znak.ico")
window.configure(background = "black")
window.title("Приветствие")
window.geometry("500x300")

logo = PhotoImage(file = "logo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 150, y = 20, width = 200, height = 150)

label1 = Label(text="Введите ваше имя: ")
label1.place(x=30, y=200, width=120, height=25)

textbox1 = Entry(text="")
textbox1.place(x=200, y=200, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text="Нажать", command=click)
button1.place(x=30, y=230, width=120, height=25)

textbox2 = Message(text="")
textbox2.place(x=200, y=230, width=200, height=25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"
window.mainloop()