'''
import tkinter as tk
import tkinter.ttk as ttk
import time
from threading import Thread, Timer


class Pomodoro:
    def __init__(self, study_interval, break_interval):
        self.study_interval = study_interval
        self.break_interval = break_interval
        self.is_break_time = False
        self.timer = None  # To keep track of the timer thread
        self.time_left = 0  # To keep track of the time left in seconds
        self.running = True

    def start_timer(self):
        # Stop the previous timer if it exists
        if self.timer:
            self.timer.cancel()
        # Start a new timer based on the current interval
        if self.is_break_time:
            print(f"Break for {self.break_interval} minutes!")
            self.time_left = self.break_interval * 60
            self.timer = Timer(1, self.update_timer)
        else:
            print(f"Study for {self.study_interval} minutes!")
            self.time_left = self.study_interval * 60
            self.timer = Timer(1, self.update_timer)
        self.timer.start()

    def update_timer(self):
        # Update the time left and the progress bar
        global progress_bar
        self.time_left -= 1
        progress_bar['value'] = self.time_left
        if self.running:
            progress_bar['value'] = self.time_left
            print (self.time_left)
        # Check if the time is up
        if self.time_left == 0:
            self.toggle_break()
        else:
            # Start another timer for one second
            self.timer = Timer(1, self.update_timer)
            self.timer.start()

    def toggle_break(self):
        # Toggle the break flag and start a new timer
        self.is_break_time = not self.is_break_time
        self.start_timer()

    def add_five_minutes(self):
        # Add five minutes to the current interval and start a new timer
        if self.is_break_time:
            self.break_interval += 5
        else:
            self.study_interval += 5
        self.start_timer()

    def skip_to_break(self):
        # Set the break flag to True and start a new timer
        self.is_break_time = True
        self.start_timer()

    def skip_to_study(self):
        # Set the break flag to False and start a new timer
        self.is_break_time = False
        self.start_timer()


def start_pomodoro():
    study_interval = int(study_interval_entry.get())
    break_interval = int(break_interval_entry.get())
    pomodoro = Pomodoro(study_interval, break_interval)
    # Store the pomodoro object as a global variable
    global pomodoro_obj
    pomodoro_obj = pomodoro
    pomodoro.start_timer()



def add_five_minutes():
    # Call the add_five_minutes method of the pomodoro object
    global pomodoro_obj
    if pomodoro_obj:
        pomodoro_obj.add_five_minutes()


def skip_to_break():
    # Call the skip_to_break method of the pomodoro object
    global pomodoro_obj
    if pomodoro_obj:
        pomodoro_obj.skip_to_break()


def skip_to_study():
    # Call the skip_to_study method of the pomodoro object
    global pomodoro_obj
    if pomodoro_obj:
        pomodoro_obj.skip_to_study()


class Main(tk.Tk):
    def __init__(self):
        # Existing code
        # ...

        # Bind a function to the window closing event
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # Define the on_closing function
    def on_closing(self):
        # Set the flag to False
        pomodoro_obj.running = False
        # Wait for the thread to finish
        pomodoro_obj.timer.join()
        # Destroy the window
        self.destroy()


# Create a new Tkinter window
window = tk.Tk()

# Create the input fields
study_interval_label = tk.Label(window, text="Study interval (minutes):")
study_interval_entry = tk.Entry(window)
break_interval_label = tk.Label(window, text="Break interval (minutes):")
break_interval_entry = tk.Entry(window)

# Create the start button
start_button = tk.Button(window, text="Start Pomodoro", command=start_pomodoro)

# Create the add five minutes button
add_button = tk.Button(window, text="Add 5 minutes", command=add_five_minutes)

# Create the skip to break button
skip_break_button = tk.Button(window, text="Skip to break", command=skip_to_break)

# Create the skip to study button
skip_study_button = tk.Button(window, text="Skip to study", command=skip_to_study)

# Create the progress bar
progress_bar = tk.ttk.Progressbar(window, orient=tk.HORIZONTAL, length=300, mode='determinate')

# Add the widgets to the window
study_interval_label.pack()
study_interval_entry.pack()
break_interval_label.pack()
break_interval_entry.pack()can you
start_button.pack()
add_button.pack()
skip_break_button.pack()
skip_study_button.pack()
progress_bar.pack()

# Start the Tkinter event loop
window.mainloop()
'''

# Import the Flask module
from flask import Flask, render_template, request
import json


class Pomodoro:
    def __init__(self, study_interval, break_interval):
        self.study_interval = study_interval
        self.break_interval = break_interval
        self.is_break_time = False
        self.timer = None  # To keep track of the timer thread
        self.time_left = 0  # To keep track of the time left in seconds
        self.running = True


# Create a Flask app object
app = Flask(__name__)

# Define a global variable to store the pomodoro object
pomodoro_obj = None


# Define a route for the home page
@app.route("/")
def home():
    # Render the home.html template and pass the pomodoro object as a variable
    return render_template("home.html", pomodoro=pomodoro_obj)


# Define a route for the start_pomodoro function
@app.route("/start_pomodoro")
def start_pomodoro():
    # Get the study and break intervals from the query parameters
    study_interval = int(request.args.get("study_interval"))
    break_interval = int(request.args.get("break_interval"))
    # Create a pomodoro object and store it in the global variable
    global pomodoro_obj
    pomodoro_obj = Pomodoro(study_interval, break_interval)
    # Start the pomodoro timer
    pomodoro_obj.start_timer()
    # Return a success message
    return "Pomodoro started!"


# Define a route for the add_five_minutes function
@app.route("/add_five_minutes")
def add_five_minutes():
    # Call the add_five_minutes method of the pomodoro object
    global pomodoro_obj
    if pomodoro_obj:
        pomodoro_obj.add_five_minutes()
    # Return a success message
    return "Five minutes added!"


# Define a route for the skip_to_break function
@app.route("/skip_to_break")
def skip_to_break():
    # Call the skip_to_break method of the pomodoro object
    global pomodoro_obj
    if pomodoro_obj:
        pomodoro_obj.skip_to_break()
    # Return a success message
    return "Skipped to break!"


# Define a route for the skip_to_study function
@app.route("/skip_to_study")
def skip_to_study():
    # Call the skip_to_study method of the pomodoro object
    global pomodoro_obj
    if pomodoro_obj:
        pomodoro_obj.skip_to_study()
    # Return a success message
    return "Skipped to study!"

    def to_json(self):
        # Convert the pomodoro object to a JSON object
        return json.dumps({
            "study_interval": self.study_interval,
            "break_interval": self.break_interval,
            "is_break_time": self.is_break_time,
            "time_left": self.time_left
        })

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
