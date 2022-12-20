import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

# Create a  database
conn = sqlite3.connect('farm.db')
# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE if not exists USERS(
username text)
""")

# Commit the changes
conn.commit()

# CLOSE
conn.close()

def grab_all(self):
    # Create a  database
    conn = sqlite3.connect('farm.db')
    # Create a cursor
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM farm.db")
    records = cursor.fetchall()

    # Commit the changes
    conn.commit()

    # CLOSE
    conn.close()

    # Loop
    for record in records:
        self.

def save_it(self):
    # Create a  database
    conn = sqlite3.connect('farm.db')
    # Create a cursor
    cursor = conn.cursor()

    # Delete
    c.execute('DELETE FROM USERS;',)
    items = []
    for index in range(self.mylist_listWidget.count()):
        items.append(self.mylist_listWidget.item(index))

    for item in items:
        c.execute("INSERT INTO USERS VALUES (:items"),
        {
            'item': item.text(),
        }
        )
    # Commit the changes
    conn.commit()

    # CLOSE
    conn.close()
