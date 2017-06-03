import tkinter as tk
import view.application

class View():
    def __init__(self):
        root = tk.Tk()
        self.app = view.application.Application(tkinter=root, master_view=self)

    def register_observer(self, presenter):
        self.presenter = presenter

    def start(self):
        self.app.mainloop()

    def set_idle_state(self):
        self.set_paused_state()
        self.app.btn_stop["state"] = "disabled"

    def set_paused_state(self):
        self.app.btn_startpause["text"] = "Start"

    def set_running_state(self):
        self.app.btn_startpause["text"] = "Pause"
        self.app.btn_stop["state"] = "normal"

    # Widget interaction handlers

    def handle_startpause(self):
        self.presenter.process_startpause()

    def handle_stop(self):
        self.presenter.process_stop()




