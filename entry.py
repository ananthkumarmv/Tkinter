from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()

# Enter Your Name: default text inside the textbox 
e.insert(0, "Enter Your Name: ") #0 ---> Index number

def myClick():
	hello = "Hello " + e.get()[17:]
	myLabel = Label(root, text = hello)
	myLabel.pack()


myButton = Button(root, text = "Enter Your Name!", command=myClick, fg="blue", bg = "#000000")  # , state = DISABLED, padx=50, pady=50
myButton.pack()

root.mainloop()
