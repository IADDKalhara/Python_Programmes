import sqlite3

database = "customers.db"       # Make it easy to change database

# Print all items in database
def show_data():
    file = sqlite3.connect(database)
    nav = file.cursor()
    
    nav.execute("SELECT rowid, * from customer")
    items = nav.fetchall()
    for item in items:
        print(*item, sep="\t\t")        # Printing with a doubletab seperator

    # Commiting and closing file
    file.commit()
    file.close()

# Add single item to database
def add_one(first, last, email):
    file = sqlite3.connect(database)
    nav = file.cursor()
    
    nav.execute("INSERT INTO customer VALUES (?,?,?)", (first, last, email))
    file.commit()
    file.close()

# Delete a row from table
def remove_one(rowid):
    file = sqlite3.connect(database)
    nav = file.cursor()

    nav.execute("DELETE FROM customer WHERE rowid = ?", rowid)

    file.commit()
    file.close()


# Add many item to database
def add_many(list):
    file = sqlite3.connect(database)
    nav = file.cursor()
    
    nav.executemany("INSERT INTO customer VALUES (?,?,?)", (list))
    file.commit()
    file.close()

# Search email
def search_email(email):
    file = sqlite3.connect(database)
    nav = file.cursor()
    
    nav.execute("SELECT rowid, * FROM customer WHERE email = ?", (email,))     # Commaat the end of email makes it a tuple
    items = nav.fetchall()

    for item in items:
        print(*item, sep="\t\t")        # Printing with a doubletab seperator

    file.commit()
    file.close()


# search_email("noname@email.com")

show_data()
# remove_one('7')     # Must enter rowid in quotation marks
