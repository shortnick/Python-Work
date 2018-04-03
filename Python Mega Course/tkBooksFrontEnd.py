"""
Program stores info about a book
Title, Author
Year, ISBN


User can:

-View all records
- Search for an entry
- Add an entry
- Update an entry
- Delete an entry
- Close program

"""
from tkinter import *
import tkBooksBackEnd as backend

def get_selected_row(event):
	try:
		global selected_tuple
		#this function takes any click event in the Listbox, using part of the returned tuple (that's index).
		
		index=listing.curselection()[0]
		#get the tuple containing the whole db row
		selected_tuple=listing.get(index)
		#following lines delete/populate fields based on clicks
		f1.delete(0,END)
		f1.insert(END, selected_tuple[1])
		f2.delete(0,END)
		f2.insert(END, selected_tuple[2])
		f3.delete(0,END)
		f3.insert(END, selected_tuple[3])
		f4.delete(0,END)
		f4.insert(END, selected_tuple[4])
	except IndexError:
		pass

def do_view():
	listing.delete(0,END)
	for row in backend.view():
		listing.insert(END, row)

def do_add():
	backend.insert(title_text.get(), auth_text.get(),year_text.get(),isbn_text.get())
	#listing.delete(0,END)
	#listing.insert(END,(title_text.get(), auth_text.get(),year_text.get(),isbn_text.get()))
	do_view()

def do_delete():
	backend.delete(selected_tuple[0])
	#clears the display fields of the deleted entry
	f1.delete(0,END)
	f2.delete(0,END)
	f3.delete(0,END)
	f4.delete(0,END)
	do_view()

def do_search():
	listing.delete(0,END)
	for row in backend.search(title_text.get(), auth_text.get(),year_text.get(),isbn_text.get()):
		listing.insert(END, row)

def do_update():
	backend.update(title_text.get(), auth_text.get(),year_text.get(),isbn_text.get())
	
	do_view()


#create the window object
window=Tk()
window.wm_title("BookCatalog")



# Labels
#==========
l1=Label(window, height=1, width=10, text="Title")
l1.grid(row=0, column=0)

l2=Label(window, height=1, width=10, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, height=1, width=10, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, height=1, width=10, text="ISBN")
l4.grid(row=1, column=2)


# Fields
#==========
title_text=StringVar()
auth_text=StringVar()
year_text=StringVar()
isbn_text=StringVar()

f1=Entry(window, textvariable=title_text, width=20)
f1.grid(row=0, column=1)

f2=Entry(window, textvariable=auth_text, width=20)
f2.grid(row=0, column=3)

f3=Entry(window, textvariable=year_text, width=20)
f3.grid(row=1, column=1)

f4=Entry(window, textvariable=isbn_text, width=20)
f4.grid(row=1, column=3)

listing=Listbox(window, height=6, width=55)
listing.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollb=Scrollbar(window)
scrollb.grid(row=2, column=2, rowspan=6)

listing.configure(yscrollcommand=scrollb.set)
scrollb.configure(command=listing.yview)

#.bind() takes two objects- an action and a function
listing.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
#==========
b1=Button(window, text="View all", width=20, command=do_view)
b1.grid(row=2, column=3)

b2=Button(window, text="Search", width=20, command=do_search)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=20, command=do_add)
b3.grid(row=4, column=3)

b4=Button(window, text="Update entry", width=20, command=do_update)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete entry", width=20, command=do_delete)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=20, command=window.destroy)
b6.grid(row=7, column=3)




window.mainloop()