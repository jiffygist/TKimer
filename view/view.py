import time
import tkinter as tk

import view.application
from presenter.presenter import Presenter, State

UPDATE_TIME_MSEC = 500

class View:
    def __init__(self):
        self.presenter = Presenter(self)
        self.tkinter = tk.Tk()
        self.app = view.application.Application(
            tkinter=self.tkinter, master_view=self)
        self.auto_update()
        self.app.mainloop()

    # Widget updaters

    def update(self, seconds, state):
        time_string = time.strftime('%H:%M:%S', time.gmtime(seconds))
        self.app.lbl_time["text"] = time_string
        self.app.btn_startpause["text"] = \
            "Pause" if state == State.RUNNING else "Start"
        self.app.btn_reset["state"] = \
            "disabled" if state == State.IDLE else "normal"

    # Widget interaction handlers

    def handle_startpause(self):
        self.presenter.handle_startpause()

    def handle_reset(self):
        self.presenter.handle_reset()

    def handle_quit(self):
        self.tkinter.destroy()

    def auto_update(self):
        self.presenter.update_time()
        self.presenter.update_view()

        # schedule timer to call myself after 1 second
        self.app.after(UPDATE_TIME_MSEC, self.auto_update)

