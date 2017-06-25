import tkinter as tk


class Application(tk.Frame):
    BUTTON_FONT = ("Arial", 16)
    LABEL_FONT = ("Helvetica", 32)

    def __init__(self, tkinter, master_view):
        super().__init__(tkinter)
        self.tkinter = tkinter
        self.master_view = master_view
        self.tkinter.title("TKimer")
        self.tkinter.protocol("WM_DELETE_WINDOW", self.master_view.handle_quit)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_time = tk.Label(self, text="00:00:00", font=self.LABEL_FONT)
        self.lbl_time.pack(side="bottom")

        self.btn_startpause = tk.Button(self)
        self.btn_startpause["text"] = "Start"
        self.btn_startpause["font"] = self.BUTTON_FONT
        self.btn_startpause["width"] = 15
        self.btn_startpause["command"] = self.master_view.handle_startpause
        self.btn_startpause.pack(side="left")

        self.btn_reset = tk.Button(self)
        self.btn_reset["text"] = "Stop"
        self.btn_reset["font"] = self.BUTTON_FONT
        self.btn_reset["command"] = self.master_view.handle_reset
        self.btn_reset.pack(side="left")
        self.btn_reset["state"] = "disabled"

        #self.quit = tk.Button(self, text="Quit", fg="red", font=self.BUTTON_FONT,
        #                      command=self.master_view.handle_quit)
        #self.quit.pack(side="right")
