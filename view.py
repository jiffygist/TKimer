import time
import tkinter as tk

import application
from state import State
from presenter import Presenter

UPDATE_TIME_MSEC = 500


class View:

    def __init__(self):
        self.presenter = Presenter(self)
        self.tkinter = tk.Tk()
        self.app = application.Application(tkinter=self.tkinter, view=self)
        self.auto_update()
        self.app.mainloop()

    def update(self, seconds, state):
        time_string = time.strftime('%H:%M:%S', time.gmtime(seconds))
        is_running = state == State.RUNNING
        is_idle = state == State.IDLE
        self.app.update_widgets(time_string, is_running, is_idle)

    def auto_update(self):
        self.presenter.update_time()
        self.presenter.update_view()

        # schedule a call to auto_update() after some time interval
        self.app.after(UPDATE_TIME_MSEC, self.auto_update)

    # Widget interaction handlers

    def handle_startpause(self):
        self.presenter.handle_startpause()

    def handle_reset(self):
        self.presenter.handle_reset()

    def handle_quit(self):
        self.tkinter.destroy()
