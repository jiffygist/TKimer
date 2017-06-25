import time
from enum import Enum

# from model.model import Model


class State(Enum):
    RUNNING = 1
    PAUSED = 2
    IDLE = 3


class Presenter:
    def __init__(self, view):
        self.view = view
        # self.model = Model()
        self.reset_time()
        self.state = State.IDLE

    def handle_startpause(self):
        if self.state == State.IDLE or self.state == State.PAUSED:
            self.start_time = time.time()
            self.state = State.RUNNING
        elif self.state == State.RUNNING:
            self.update_time()
            self.state = State.PAUSED
        self.update_view()

    def handle_reset(self):
        self.reset_time()
        self.state = State.IDLE
        self.update_view()

    def reset_time(self):
        self.time = 0.0

    def update_time(self):
        if self.state == State.RUNNING:
            current_time = time.time()
            self.time += current_time - self.start_time
            self.start_time = current_time

    def update_view(self):
        self.view.update(int(self.time), self.state)
