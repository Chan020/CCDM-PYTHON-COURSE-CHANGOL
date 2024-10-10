import MySQLdb

#IMPORTING A CSV FILE INTO EXISTING TABLE IN WORK BENCH

import csv

#Create a connection
myconnection = MySQLdb.Connection(host = "localhost", user = "root", password = "ceit")

#Create a cursor object used to hold connection
mycursor = myconnection.cursor()

#Now let's start with SQL queries
#mycursor.execute('CREATE DATABASE CEITLIBRARY')
mycursor.execute('USE CEITLIBRARY')
tablebook = """CREATE TABLE book(bookID int primary key, title varchar(20), author varchar(20), genre varchar(20))"""

#Create another table
mycursor.execute('USE CEITLIBRARY')
tableborrower = """CREATE TABLE borrower(borrowerID int primary key, Firstname varchar(20), curname varchar(20), Course varchar(20))"""

#To execute Tablebook
#mycursor.execute(tableborrower)
#mycursor.execute(tableborrower)
#INSERTING RECORDS INTO BOOK TABLE
#book1 = """INSERT INTO book VALUES(101, "Intro to Python", "Surname", "Programming")"""
#INSERTING RECORDS INTO BORROWERS TABLE
#Borrower1 = """INSERT INTO borrower VALUES(1004, "Thomas", "Powai", "MathsScience")"""
#mycursor.execute(Borrower1)
#mycursor.execute(book1)
#mycursor.execute('SHOW DATABASES')

file = open('Book.csv')
contents = csv.reader(file)
insertVal = "INSERT INTO book (bookID, title, author,genre) VALUES (?,?,?,?)""
mycursor.executemany(insertVal,contents)
selectall = "SELECT * FROM book"

rows = mycursor.execute(selectall).fetchall()
for row in rows:

#To fetch data and display output
#result = mycursor.fetchall()

#Commit changes
myconnection.commit()
myconnection.close

for row in result:
    print(row)