'''
import tkinter as tk
from tkinter import messagebox
import requests
import json
import database

def create_study_session():

    # Get the input values
    student_email = student_email_entry.get()
    goals = goals_entry.get().split(',')
    study_interval = int(study_interval_entry.get())
    break_interval = int(break_interval_entry.get())

    # Define the study session data
    session_data = {
        'student_email': student_email,
        'goals': goals,
        'study_interval': study_interval,
        'break_interval': break_interval
    }

    # Send a POST request to the create_study_session route
    response = requests.post('http://localhost:5000/create_study_session', data=json.dumps(session_data))

    # Check the response status code and data
    if response.status_code == 200:
        messagebox.showinfo("Success", "Study session created successfully")
    else:
        messagebox.showerror("Error", "Failed to create study session")


# Create a new Tkinter window
window = tk.Tk()

import database

# Create a connection to the database
conn = database.create_connection()

# Create the students table
database.create_table(conn)

# Insert a student
database.insert_student(conn, 'student@example.com', 'Test Student', 'Math, Science')

# Get a student
student = database.get_student(conn, 'student@example.com')
print(student)

# Get all students
students = database.get_all_students(conn)
print(students)

# Update a student
database.update_student(conn, 'student@example.com', 'Updated Student', 'Math, Science, English')

# Delete a student
database.delete_student(conn, 'student@example.com')



# Create the labels and input fields
student_email_label = tk.Label(window, text="Student email")
student_email_entry = tk.Entry(window)
goals_label = tk.Label(window, text="Goals")
goals_entry = tk.Entry(window)
study_interval_label = tk.Label(window, text="Study Interval")
study_interval_entry = tk.Entry(window)
break_interval_label = tk.Label(window, text="Break Interval")
break_interval_entry = tk.Entry(window)

# Create the submit button
submit_button = tk.Button(window, text="Create Study Session", command=create_study_session)

# Add the wemailgets to the window
student_email_label.pack()
student_email_entry.pack()
goals_label.pack()
goals_entry.pack()
study_interval_label.pack()
study_interval_entry.pack()
break_interval_label.pack()
break_interval_entry.pack()
submit_button.pack()

# Start the Tkinter event loop
window.mainloop()
'''

import tkinter as tk
from tkinter import messagebox
import requests
import json
import database

def create_study_session():
    # Get the input values
    student_email = student_email_entry.get()
    goals = goals_entry.get().split(',')
    study_interval = int(study_interval_entry.get())
    break_interval = int(break_interval_entry.get())
    courses = courses_entry.get().split(',')

    # Define the study session data
    session_data = {
        'student_email': student_email,
        'goals': goals,
        'study_interval': study_interval,
        'break_interval': break_interval,
        'courses': courses
    }

    # Send a POST request to the create_study_session route
    response = requests.post('http://localhost:5000/create_study_session', data=json.dumps(session_data))

    # Check the response status code and data
    if response.status_code == 200:
        messagebox.showinfo("Success", "Study session created successfully")
    else:
        messagebox.showerror("Error", "Failed to create study session")

# Create a new Tkinter window
window = tk.Tk()

# Create the labels and input fields
student_email_label = tk.Label(window, text="Student email")
student_email_entry = tk.Entry(window)
goals_label = tk.Label(window, text="Goals")
goals_entry = tk.Entry(window)
study_interval_label = tk.Label(window, text="Study Interval")
study_interval_entry = tk.Entry(window)
break_interval_label = tk.Label(window, text="Break Interval")
break_interval_entry = tk.Entry(window)
courses_label = tk.Label(window, text="Courses")
courses_entry = tk.Entry(window)

# Create the submit button
submit_button = tk.Button(window, text="Create Study Session", command=create_study_session)

# Add the widgets to the window
student_email_label.pack()
student_email_entry.pack()
goals_label.pack()
goals_entry.pack()
study_interval_label.pack()
study_interval_entry.pack()
break_interval_label.pack()
break_interval_entry.pack()
courses_label.pack()
courses_entry.pack()
submit_button.pack()

# Start the Tkinter event loop
window.mainloop()
