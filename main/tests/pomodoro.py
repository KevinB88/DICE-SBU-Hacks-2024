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
break_interval_entry.pack()
start_button.pack()
add_button.pack()
skip_break_button.pack()
skip_study_button.pack()
progress_bar.pack()

# Start the Tkinter event loop
window.mainloop()
