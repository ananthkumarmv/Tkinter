from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text = "Look I Clicked a Button!!")
	myLabel.pack()


myButton = Button(root, text = "Click Me!", command=myClick, fg="blue", bg = "#000000")  # , state = DISABLED, padx=50, pady=50
myButton.pack()


root.mainloop()
