from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Title goes here")
root.iconbitmap('Images/codemy.ico')

def open():
	global my_img
	top = Toplevel()
	top.title("My Second Window")
	top.iconbitmap('Images/toys.png')
	# lbl = Label(top, text="Hello World").pack()
	my_img = ImageTk.PhotoImage(Image.open('Images/toys.png'))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()



btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()

