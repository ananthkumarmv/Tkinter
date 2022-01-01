from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Title goes here")
root.iconbitmap('Images/codemy.ico')
root.geometry("400x400")

# Databases


# Create a datanbase or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()


# Create table
c.execute("""CREATE TABLE addresses(
			first_name text, 
			last_name text,
			address text,
			city text,
			state text,
			zipcode integer)""")

#Commit Changes
conn.commit()

#Close COnnection
conn.close()


root.mainloop()
