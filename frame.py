from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Title goes here")
root.iconbitmap('Images/codemy.ico')


# creating the frame
# frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50) # space inside the frame

frame = LabelFrame(root, padx=50, pady=50)

# spaces around the frame
frame.pack(padx=10, pady=10)


b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or Here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
