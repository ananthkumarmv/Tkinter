from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Title goes here")
root.iconbitmap('Images/codemy.ico')

r = IntVar()
r.set("2")


def clicked(value):
	myLable = Label(root, text=value)
	myLable.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLable = Label(root, text=r.get())
myLable.pack()



myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get())).pack()


root.mainloop()
