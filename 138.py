from tkinter import *

def click():
    art_num = textbox1.get()
    if art_num == "1" or art_num == "2" or art_num == "3" or art_num == "4" or art_num == "5" or art_num == "6" or art_num == "7":
        art_image = art_num + ".gif"
        view = PhotoImage(file=art_image)
        photobox.image = view
        photobox["image"] = view
        photobox.update()
    else:
        view = PhotoImage(file="wrong.gif")
        photobox.image = view
        photobox["image"] = view
        photobox.update()



window = Tk()
window.configure(background = "black")
window.title("Изображения по номерам")
window.geometry("560x250")

art = PhotoImage(file = "logo.gif")
photobox = Label(window, image = art)
photobox.image = art
photobox.place(x = 170, y = 20, width = 200, height = 150)

label1 = Label(text="Введите цифру: ")
label1.place(x=30, y=200, width=120, height=25)

textbox1 = Entry(text="")
textbox1.place(x=170, y=200, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text="Показать картинку", command=click)
button1.place(x=390, y=200, width=120, height=25)

window.mainloop()