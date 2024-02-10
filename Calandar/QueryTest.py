import sqlite3
from tkinter import *

# Create or connect to database
conn = sqlite3.connect('QueryTest.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (name TEXT, email TEXT)''')
conn.commit()


# Function to insert data into the database
def insert_data(name, email):
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()


# Function to handle the submit action
def submit_action():
    insert_data(name_entry.get(), email_entry.get())
    name_entry.delete(0, END)
    email_entry.delete(0, END)


# Set up the GUI
root = Tk()
root.title("User Data Entry")

# Name field
name_label = Label(root, text="Name")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

# Email field
email_label = Label(root, text="Email")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

# Submit button
submit_btn = Button(root, text="Submit", command=submit_action)
submit_btn.pack()

# Run the GUI loop
root.mainloop()

# Close the database connection before exiting
conn.close()
