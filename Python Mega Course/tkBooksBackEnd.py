#! python3

import sqlite3

def connect():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

	conn.commit()
	conn.close()

def insert(title, author, year, isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM books")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(title="", author="", year="", isbn=""):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM books WHERE id=?", (id,))
	conn.commit()
	conn.close()

def update(id,title,author, year, isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn,id))
	conn.commit()
	conn.close()

connect()
#insert("The Hobbit", "JRR Tolkien", 1984, 1243587)
#delete(2)
#update(4, "Simarillion", "JRR Tolkien", 1917, 1243589)
print(view())
#print(search(year=1984))