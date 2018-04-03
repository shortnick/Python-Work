
#! python3


import psycopg2


def create_table():

	conn=psycopg2.connect("dbname='postgres' user='basic' password='postgrescorvus' host='localhost' port='5432'")
	cur= conn.cursor()

	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	
	conn.commit()
	conn.close()

def insert(item, quantity, price):
	conn=psycopg2.connect("dbname='postgres' user='basic' password='postgrescorvus' host='localhost' port='5432'")
	cur= conn.cursor()

	cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))

	conn.commit()
	conn.close()

def view():
	conn=psycopg2.connect("dbname='postgres' user='basic' password='postgrescorvus' host='localhost' port='5432'")
	cur= conn.cursor()

	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()

	return rows

def delete(theItem):
	conn=psycopg2.connect("dbname='postgres' user='basic' password='postgrescorvus' host='localhost' port='5432'")
	cur= conn.cursor()

	cur.execute("DELETE FROM store WHERE item=%s", (theItem,))
	conn.commit()
	conn.close()

def update(theQuant, thePrice, theItem):
	conn=psycopg2.connect("dbname='postgres' user='basic' password='postgrescorvus' host='localhost' port='5432'")
	cur= conn.cursor()

	cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (theQuant, thePrice, theItem))
	conn.commit()
	conn.close()




create_table()

#insert("Water Glass",10, 5)
#insert("Coffee Cup",20, 4)
#insert("Plate (x2)", 15, 10)

#delete("Coffee Cup")
#delete("Water Glass")
#update(18,5,"Coffee Cup")

print(view())
