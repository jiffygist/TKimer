from state import State
from timer import Timer
# from model import Model


class Presenter:
    def __init__(self, view):
        self.view = view
        # self.model = Model()
        self.timer = Timer()
        self.state = State.IDLE

    def handle_startpause(self):
        if self.state == State.IDLE or self.state == State.PAUSED:
            self.timer.start()
            self.state = State.RUNNING
        elif self.state == State.RUNNING:
            self.update_time()
            self.state = State.PAUSED
        self.update_view()

    def handle_reset(self):
        self.timer.reset()
        self.state = State.IDLE
        self.update_view()

    def update_time(self):
        if self.state == State.RUNNING:
            self.timer.move_forward()

    def update_view(self):
        self.view.update(int(self.timer.get_time()), self.state)
