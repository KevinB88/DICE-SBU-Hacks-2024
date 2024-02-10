class Session:
    def __init__(self, id, student_id, goals, study_interval, break_interval):
        self.id = id
        self.student_id = student_id
        self.goals = goals
        self.study_interval = study_interval
        self.break_interval = break_interval
        self.status = "ongoing"
        self.time_logged = 0

    def log_time(self, time):
        # Log time for the session
        self.time_logged += time

    def complete(self):
        # Mark the session as completed
        self.status = "completed"

    def get_commit(self):
        # Generate a commit for the session
        commit = {
            "id": self.id,
            "student_id": self.student_id,
            "goals": self.goals,
            "study_interval": self.study_interval,
            "break_interval": self.break_interval,
            "status": self.status,
            "time_logged": self.time_logged
        }
        return commit
