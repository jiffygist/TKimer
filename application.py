import tkinter as tk

BUTTON_START_NAME = "Start"
BUTTON_PAUSE_NAME = "Pause"
BUTTON_RESET_NAME = "Reset"


class Application(tk.Frame):

    BUTTON_FONT = ("Arial", 16)
    LABEL_FONT = ("Helvetica", 32)

    def __init__(self, tkinter, view):
        super().__init__(tkinter)
        self.tkinter = tkinter
        self.view = view
        self.tkinter.title("TKimer")
        self.tkinter.protocol("WM_DELETE_WINDOW", self.view.handle_quit)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_time = tk.Label(self, text="00:00:00", font=self.LABEL_FONT)
        self.lbl_time.pack(side="bottom")

        self.btn_startpause = tk.Button(self)
        self.btn_startpause["text"] = BUTTON_START_NAME
        self.btn_startpause["font"] = self.BUTTON_FONT
        self.btn_startpause["width"] = 15
        self.btn_startpause["command"] = self.view.handle_startpause
        self.btn_startpause.pack(side="left")

        self.btn_reset = tk.Button(self)
        self.btn_reset["text"] = BUTTON_RESET_NAME
        self.btn_reset["font"] = self.BUTTON_FONT
        self.btn_reset["command"] = self.view.handle_reset
        self.btn_reset.pack(side="left")
        self.btn_reset["state"] = "disabled"

    def update_widgets(self, time_string, is_running, is_idle):
        self.lbl_time["text"] = time_string
        self.btn_startpause["text"] = \
            BUTTON_PAUSE_NAME if is_running else BUTTON_START_NAME
        self.btn_reset["state"] = "disabled" if is_idle else "normal"
