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


# Function to fetch data from the database
def fetch_data():
    c.execute("SELECT * FROM users")
    return c.fetchall()


# Function to handle the fetch action
def fetch_action():
    data = fetch_data()

    # Create a new window to display the fetched data
    data_window = Toplevel(root)
    data_window.title("Fetched Data")

    # Add column headers
    Label(data_window, text="Name", font=('bold', 14)).grid(row=0, column=0)
    Label(data_window, text="Email", font=('bold', 14)).grid(row=0, column=1)

    # Display the data in a grid
    for index, (name, email) in enumerate(data, start=1):
        Label(data_window, text=name).grid(row=index, column=0)
        Label(data_window, text=email).grid(row=index, column=1)


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
submit_btn = Button(root, text="Submit", command=lambda: submit_action())
submit_btn.pack()

# Fetch Data button
fetch_btn = Button(root, text="Fetch Data", command=fetch_action)
fetch_btn.pack()


def submit_action():
    insert_data(name_entry.get(), email_entry.get())
    name_entry.delete(0, END)
    email_entry.delete(0, END)


# Run the GUI loop
root.mainloop()

# Close the database connection before exiting
conn.close()
