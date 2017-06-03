import time
import tkinter as tk

import view.application


class View:
    def __init__(self):
        self.tkinter = tk.Tk()
        self.app = view.application.Application(tkinter=self.tkinter, master_view=self)

    def register_observer(self, presenter):
        self.presenter = presenter

    def start(self):
        self.app.mainloop()

    # Widget updaters

    def update_clock(self, seconds):
        time_string = time.strftime('%H:%M:%S', time.gmtime(seconds))
        self.app.lbl_time["text"] = time_string

    def set_idle_state(self):
        self.set_paused_state()
        self.app.btn_stop["state"] = "disabled"

    def set_paused_state(self):
        self.app.btn_startpause["text"] = "Start"

    def set_running_state(self):
        self.app.btn_startpause["text"] = "Pause"
        self.app.btn_stop["state"] = "normal"

    # Widget interaction handlers

    def handle_update_clock(self):
        self.presenter.process_update_clock()

    def handle_startpause(self):
        self.presenter.process_startpause()

    def handle_stop(self):
        self.presenter.process_stop()

    def handle_quit(self):
        self.tkinter.destroy()
        self.presenter.process_quit()
