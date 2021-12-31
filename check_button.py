from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title goes here")
root.iconbitmap('Images/codemy.ico')
root.geometry("400x400")


var = IntVar()

c = Checkbutton(root, text="Check this box", variable=var)
c.pack()



root.mainloop()