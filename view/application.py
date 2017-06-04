import tkinter as tk


class Application(tk.Frame):
    def __init__(self, tkinter, master_view):
        super().__init__(tkinter)
        self.tkinter = tkinter
        self.master_view = master_view
        self.tkinter.title("TKimer")
        self.tkinter.protocol("WM_DELETE_WINDOW", self.master_view.handle_quit)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_time = tk.Label(text="00:00:00")
        self.lbl_time.pack(side="top")

        self.btn_startpause = tk.Button(self)
        self.btn_startpause["text"] = "Start"
        self.btn_startpause["command"] = self.master_view.handle_startpause
        self.btn_startpause.pack(side="left")

        self.btn_stop = tk.Button(self)
        self.btn_stop["text"] = "Stop"
        self.btn_stop["command"] = self.master_view.handle_stop
        self.btn_stop.pack(side="left")
        self.btn_stop["state"] = "disabled"

        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.master_view.handle_quit)
        self.quit.pack(side="right")
