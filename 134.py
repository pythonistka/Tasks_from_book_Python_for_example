from tkinter import *
import random
from tkinter import PhotoImage


def checkans():
    theirans = ansbox.get()
    theirans = int(theirans)
    num1 = num1box["text"]
    num1 = int(num1)
    num2 = num2box["text"]
    num2 = int(num2)
    ans = num1 + num2
    if theirans == ans:
        image1 = PhotoImage(file="correct.gif")
        imgbx.image = image1
        imgbx["image"] = image1
        imgbx.update()
    else:
        image2 = PhotoImage(file="wrong.gif")
        imgbx.image = image2
        imgbx["image"] = image2
        imgbx.update()


def nextquestion():
    ansbox.delete(0, END)
    num1 = random.randint(10, 50)
    num1box["text"] = num1
    num2 = random.randint(10, 50)
    num2box["text"] = num2
    image1 = PhotoImage(file="logo.gif")
    imgbx.image = image1
    imgbx["image"] = image1
    imgbx.update()


window = Tk()
window.title("Addition")
window.geometry("250x300")

num1box = Label(text="0")
num1box.place(x=50, y=30, width=25, height=25)

addsymbl = Message(text="+")
addsymbl.place(x=75, y=30, width=25, height=25)

num2box = Label(text="0")
num2box.place(x=100, y=30, width=25, height=25)

eqlsymbl = Message(text="=")
eqlsymbl.place(x=125, y=30, width=25, height=25)

ansbox = Entry(text="")
ansbox.place(x=150, y=30, width=25, height=25)
ansbox["justify"] = "center"
ansbox.focus()

checkbtn = Button(text="Check", command=checkans)
checkbtn.place(x=50, y=60, width=75, height=25)

nextbtn = Button(text="Next", command=nextquestion)
nextbtn.place(x=130, y=60, width=75, height=25)

image = PhotoImage(file="logo.gif")
imgbx = Label(image=image)
imgbx.image = image
imgbx.place(x=25, y=100, width=200, height=150)

nextquestion()
window.mainloop()
