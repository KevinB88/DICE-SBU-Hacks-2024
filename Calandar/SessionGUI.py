import tkinter as tk
from tkinter import messagebox


class Session:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Session Tracker")

        # Session attributes inputs
        self.id_entry = self.create_input_field("Session ID:")
        self.student_id_entry = self.create_input_field("Student ID:")
        self.goals_entry = self.create_input_field("Goals:")
        self.study_interval_entry = self.create_input_field("Study Interval (mins):")
        self.break_interval_entry = self.create_input_field("Break Interval (mins):")

        # Buttons for actions
        self.create_session_btn = tk.Button(root, text="Create Session", command=self.create_session)
        self.create_session_btn.pack(pady=(10, 5))

        self.log_time_btn = tk.Button(root, text="Log Time (mins)", command=self.log_time)
        self.log_time_btn.pack(pady=5)

        self.complete_session_btn = tk.Button(root, text="Complete Session", command=self.complete_session)
        self.complete_session_btn.pack(pady=5)

        self.view_session_btn = tk.Button(root, text="View Session Details", command=self.view_session_details)
        self.view_session_btn.pack(pady=(5, 10))

        # Initialize session object as None
        self.session = None

    def create_input_field(self, label):
        """Utility function to create label and entry fields."""
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text=label).pack(side=tk.LEFT)
        entry = tk.Entry(frame)
        entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
        return entry

    # Define actions
    def create_session(self):
        # Create a new Session instance with input values
        try:
            self.session = Session(
                id=int(self.id_entry.get()),
                student_id=self.student_id_entry.get(),
                goals=self.goals_entry.get(),
                study_interval=int(self.study_interval_entry.get()),
                break_interval=int(self.break_interval_entry.get())
            )
            messagebox.showinfo("Success", "Session created successfully!")
        except ValueError as e:
            messagebox.showerror("Error", "Please ensure all fields are correctly filled.")

    def log_time(self):
        if self.session:
            # Log time for the session
            time = simpledialog.askinteger("Log Time", "Enter time in minutes:", parent=self.root)
            if time:
                self.session.log_time(time)
                messagebox.showinfo("Success", "Time logged successfully!")
        else:
            messagebox.showerror("Error", "No session created.")

    def complete_session(self):
        if self.session:
            self.session.complete()
            messagebox.showinfo("Success", "Session marked as completed.")
        else:
            messagebox.showerror("Error", "No session created.")

    def view_session_details(self):
        if self.session:
            commit = self.session.get_commit()
            details = "\n".join(f"{key}: {value}" for key, value in commit.items())
            messagebox.showinfo("Session Details", details)
        else:
            messagebox.showerror("Error", "No session created.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SessionGUI(root)
    root.mainloop()
