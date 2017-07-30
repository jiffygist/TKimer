from state import State
from button import Button
from timer import Timer
# from model import Model


class Presenter:
    def __init__(self, view):
        self.view = view
        # self.model = Model()
        self.timer = Timer()
        self.state = State.IDLE

        self.dispatch_table = {
            # Format: (button, current_state) : (action, new_state)
            (Button.START, State.IDLE): (self.do_run, State.RUNNING),
            (Button.START, State.RUNNING): (self.do_pause, State.PAUSED),
            (Button.START, State.PAUSED): (self.do_run, State.RUNNING),
            (Button.RESET, State.IDLE): (self.do_reset, State.IDLE),
            (Button.RESET, State.RUNNING): (self.do_reset, State.IDLE),
            (Button.RESET, State.PAUSED): (self.do_reset, State.IDLE)
        }

    def update_time(self):
        if self.state == State.RUNNING:
            self.timer.update()

    def update_view(self):
        self.view.update(self.timer.get_seconds(), self.state)

    def do_run(self):
        self.timer.start()

    def do_pause(self):
        self.update_time()

    def do_reset(self):
        self.timer.reset()

    def handle_event(self, button):
        action, new_state = self.dispatch_table[(button, self.state)]
        action()
        self.state = new_state
        self.update_view()
