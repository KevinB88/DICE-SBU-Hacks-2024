import tkinter as tk
from tkinter import messagebox
import requests
import json

def create_study_session():
    # Get the input values
    student_id = student_id_entry.get()
    goals = goals_entry.get().split(',')
    study_interval = int(study_interval_entry.get())
    break_interval = int(break_interval_entry.get())

    # Define the study session data
    session_data = {
        'student_id': student_id,
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

# Create the labels and input fields
student_id_label = tk.Label(window, text="Student ID")
student_id_entry = tk.Entry(window)
goals_label = tk.Label(window, text="Goals")
goals_entry = tk.Entry(window)
study_interval_label = tk.Label(window, text="Study Interval")
study_interval_entry = tk.Entry(window)
break_interval_label = tk.Label(window, text="Break Interval")
break_interval_entry = tk.Entry(window)

# Create the submit button
submit_button = tk.Button(window, text="Create Study Session", command=create_study_session)

# Add the widgets to the window
student_id_label.pack()
student_id_entry.pack()
goals_label.pack()
goals_entry.pack()
study_interval_label.pack()
study_interval_entry.pack()
break_interval_label.pack()
break_interval_entry.pack()
submit_button.pack()

# Start the Tkinter event loop
window.mainloop()
