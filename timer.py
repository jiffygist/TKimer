import time


class Timer:

    def __init__(self):
        self.reset()

    def reset(self):
        self.time = 0.0

    def start(self):
        self.start_time = time.time()

    def update(self):
        current_time = time.time()
        self.time += current_time - self.start_time
        self.start_time = current_time

    def get_seconds(self):
        return int(self.time)