def is_waking_hours(current_time, waking_hours):
    pass


def is_during_class(current_time, schedule):
    pass


class Session:
    def __init__(self, email, student_email, goals, study_interval, break_interval):
        self.email = email
        self.student_email = student_email
        self.goals = goals
        self.study_interval = study_interval
        self.break_interval = break_interval
        self.status = "ongoing"
        self.time_logged = 0

    def log_time(self, time):
        # Log time for the session
        self.time_logged += time

    def generate_study_times(self, exam_time, waking_hours, session_length, num_sessions=None):
        study_times = []

        # Start from the day of the exam and work backwards
        current_time = exam_time
        while len(study_times) < num_sessions:
            # Check if the current time is during waking hours and not during a class
            if is_waking_hours(current_time, waking_hours) and not is_during_class(current_time, self):
                # If so, add a study session
                study_times.append(current_time)
                # And move to the next potential study session
                current_time -= session_length + self.break_interval
            else:
                # If not, move to the next potential study session
                current_time -= session_length

        return study_times

    def complete(self):
        # Mark the session as completed
        self.status = "completed"

    def get_commit(self):
        # Generate a commit for the session
        commit = {
            "email": self.email,
            "student_email": self.student_email,
            "goals": self.goals,
            "study_interval": self.study_interval,
            "break_interval": self.break_interval,
            "status": self.status,
            "time_logged": self.time_logged
        }
        return commit
