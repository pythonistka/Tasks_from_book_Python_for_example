import random
from tkinter import *

def click():
    num = random.randint(1, 6)
    textbox["bg"] = "yellow"
    textbox["fg"] = "blue"
    textbox["text"] = num

window = Tk()
window.geometry("400x150")

button1 = Button(text="Press me", command=click)
button1.place(x=30, y=50, width=110, height=25)

textbox = Message(text="")
textbox.place(x=150, y=50, width=190, height=25)
textbox["bg"] = "white"
textbox["fg"] = "black"
window.mainloop()