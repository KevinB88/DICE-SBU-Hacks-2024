import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (name TEXT, email TEXT, hobbies TEXT)''')
conn.commit()


def open_hobbies_window(name, email):
    hobbies_window = tk.Toplevel()
    hobbies_window.title("Hobbies Input")

    tk.Label(hobbies_window, text="Enter your hobbies, separated by commas:").pack()
    hobbies_entry = tk.Entry(hobbies_window, width=50)
    hobbies_entry.pack()

    submit_hobbies_btn = tk.Button(hobbies_window, text="Submit Hobbies",
                                   command=lambda: submit_hobbies(name, email, hobbies_entry.get()))
    submit_hobbies_btn.pack()


def submit_name_email(name, email):
    print(f"Name: {name}, Email: {email}")
    open_hobbies_window(name, email)  # Pass name and email to the next window


def submit_hobbies(name, email, hobbies):
    hobbies_list = ', '.join([hobby.strip() for hobby in hobbies.split(',')])
    print("Hobbies:", hobbies_list)
    # Insert data into the database
    c.execute("INSERT INTO users (name, email, hobbies) VALUES (?, ?, ?)", (name, email, hobbies_list))
    conn.commit()
    print("Data saved to database.")


# To delete the contents from our database

def delete_database_contents():
    # Ask for confirmation before deletion
    response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all data from the database?")
    if response:
        c.execute("DELETE FROM users")
        conn.commit()
        messagebox.showinfo("Deletion Complete", "All data has been deleted from the database.")

# Viewing the contents of our database


def view_database_contents():

    # Fetch data from the database
    c.execute("SELECT * FROM users")
    data = c.fetchall()

    # Create a new window to display the data
    data_window = tk.Toplevel()
    data_window.title("Database Contents")

    # Add column headers
    headers = ['Name', 'Email', 'Hobbies']
    for col, header in enumerate(headers):
        tk.Label(data_window, text=header, font=('bold', 14), borderwidth=2, relief='groove').grid(row=0, column=col,
                                                                                                   sticky='ew')

    # Display the data in a grid
    for row_index, row_data in enumerate(data, start=1):
        for col_index, cell in enumerate(row_data):
            tk.Label(data_window, text=cell, borderwidth=2, relief='groove').grid(row=row_index, column=col_index,
                                                                                  sticky='ew')

    # Adjust column weights to make them expandable
    for index in range(len(headers)):
        data_window.grid_columnconfigure(index, weight=1)

        '''
            function for viewing the contents of our data-base 
        '''


root = tk.Tk()
root.title("Name and Email Input")

tk.Label(root, text="Enter your name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Enter your email:").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

submit_btn = tk.Button(root, text="Submit", command=lambda: submit_name_email(name_entry.get(), email_entry.get()))
submit_btn.pack()

view_db_btn = tk.Button(root, text="View Database Contents", command=view_database_contents)
view_db_btn.pack()

delete_db_btn = tk.Button(root, text="Delete Database Contents", command=delete_database_contents)
delete_db_btn.pack()

root.mainloop()

# Close the database connection before exiting
conn.close()
