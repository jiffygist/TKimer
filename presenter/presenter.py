import threading
import time


class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.state = self.model.STATE_IDLE
        self.new_time_thread()

    def new_time_thread(self):
        self.time_thread = threading.Timer(self.model.TIMER_UPDATE_DELTA, self.process_update_clock)

    def cancel_time_thread(self):
        self.time_thread.cancel()
        self.new_time_thread()

    def process_startpause(self):
        if self.state == self.model.STATE_IDLE or self.state == self.model.STATE_PAUSED:
            self.state = self.model.STATE_RUNNING
            self.view.set_running_state()
            self.model.start_time = time.time()
            self.process_update_clock()
        elif self.state == self.model.STATE_RUNNING:
            self.state = self.model.STATE_PAUSED
            self.view.set_paused_state()
            self.cancel_time_thread()

    def process_stop(self):
        self.state = self.model.STATE_IDLE
        self.model.reset_time()
        self.cancel_time_thread()
        self.process_update_clock()
        self.view.set_idle_state()

    def process_update_clock(self):
        self.view.update_clock(self.model.get_seconds())
        if self.state == self.model.STATE_RUNNING:
            self.model.time = time.time()
            self.new_time_thread()
            self.time_thread.start()

    def process_quit(self):
        self.cancel_time_thread()
        # End of program.

    def run(self):
        self.view.start()