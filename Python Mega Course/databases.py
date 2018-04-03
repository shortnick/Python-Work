
#! python3

import sqlite3 


def create_table():

	conn=sqlite3.connect("lite.db")
	cur= conn.cursor()

	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

	

	conn.commit()
	conn.close()

def insert(item, quantity, price):
	conn=sqlite3.connect("lite.db")
	cur= conn.cursor()

	cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))

	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("lite.db")
	cur= conn.cursor()

	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()

	return rows

def delete(theItem):
	conn=sqlite3.connect("lite.db")
	cur= conn.cursor()

	cur.execute("DELETE FROM store WHERE item=?", (theItem,))
	conn.commit()
	conn.close()

def update(theQuant, thePrice, theItem):
	conn=sqlite3.connect("lite.db")
	cur= conn.cursor()

	cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (theQuant, thePrice, theItem))
	conn.commit()
	conn.close()




#insert("Water Glass",10, 5)
#insert("Coffee Cup",20, 4)

#delete("Coffee Cup")

update(18,5,"Coffee Cup")

print(view())
