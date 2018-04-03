#! python3

from tkinter import *
from sqlite3 import *

#create the window object
window=Tk()

def km_to_miles():
	print("bob")
	miles = float(e1_Value.get())*1.609344
	t1.insert(END,miles)


b1 = Button(window, text="Execute", command=km_to_miles)
#place button in window
#b1.pack() <-- more general?
b1.grid(row=0, column=0, rowspan=2)

#used for passing info around
e1_Value=StringVar()

#user entry method
e1=Entry(window, textvariable=e1_Value)
e1.grid(row=0, column=1)

#text display area
t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()

