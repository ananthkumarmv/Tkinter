from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Title goes here')
root.iconbitmap('Images/codemy.ico')

# 3 steps
my_img1 = ImageTk.PhotoImage(Image.open('Images/toys.png'))
my_img2 = ImageTk.PhotoImage(Image.open('Images/toys2.jfif'))
my_img3 = ImageTk.PhotoImage(Image.open('Images/toys3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('Images/toys4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('Images/toys5.jpeg'))

image_list = [my_img1, my_img2,my_img3,my_img4,my_img5]

image_list[2]


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()

def back():
	return




button_back = Button(root, text='<<', command=back)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='>>', command= lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()