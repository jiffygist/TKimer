class Model:
    STATE_RUNNING = "RUNNING"
    STATE_PAUSED = "PAUSED"
    STATE_IDLE = "IDLE"
    TIMER_UPDATE_DELTA = 0.03

    def __init__(self):
        self.reset_time()

    def reset_time(self):
        self.start_time = 0
        self.time = 0

    def get_seconds(self):
        return int(self.time - self.start_time)
