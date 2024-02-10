import time

class Pomodoro:
    def __init__(self, study_interval, break_interval):
        self.study_interval = study_interval
        self.break_interval = break_interval
        self.is_break_time = False

    def start_timer(self):
        while True:
            if self.is_break_time:
                print(f"Break for {self.break_interval} minutes!")
                time.sleep(self.break_interval * 60)
                self.is_break_time = False
            else:
                print(f"Study for {self.study_interval} minutes!")
                time.sleep(self.study_interval * 60)
                self.is_break_time = True
