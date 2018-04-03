"""Please create a Python program that expects a kilogram input value and converts that value to grams, pounds, and ounces when the user pushes the convert button."""

from tkinter import *


#create the window object
window=Tk()

def kg_to_imperials():
	
	pounds = round((float(e1_Value.get())*2.204623),5)
	ounces = 16*pounds
	grams = 1000*float(e1_Value.get())
	t1.insert(END, str(grams)+"g")
	t2.insert(END, str(ounces)+"oz")
	t3.insert(END, str(pounds)+"lbs")

b1 = Button(window, text="Convert", command=kg_to_imperials)
#place button in window
#b1.pack() <-- more general?
b1.grid(row=0, column=2)

#used for passing info around
e1_Value=StringVar()

#user entry method
e1=Entry(window, textvariable=e1_Value)
e1.grid(row=0, column=1)

d1=Label(window, height=1, width=20, text="Kg")
d1.grid(row=0, column=0)


#text display area
t1=Text(window, height=1, width=20)
t1.grid(row=1, column=0)

#text display area
t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)

#text display area
t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()

