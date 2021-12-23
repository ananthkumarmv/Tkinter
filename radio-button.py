from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Title goes here")
root.iconbitmap('Images/codemy.ico')

r = IntVar()
r.set("2")


TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping, in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)



def clicked(value):
	myLable = Label(root, text=value)
	myLable.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLable = Label(root, text=pizza.get())
# myLable.pack()



myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get())).pack()


root.mainloop()
