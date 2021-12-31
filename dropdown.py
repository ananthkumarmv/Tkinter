from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Title goes here")
root.iconbitmap('Images/codemy.ico')
root.geometry("400x400")

# Drop Down Boxes

def show():
	myLabel = Label(root, text=clicked.get()).pack()


options = [
			"Mon", 
			"Tue", 
			"Wed", 
			"Thu", 
			"Fri"
]

clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options)
drop.pack()


myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
 