import tkinter as tk

class Application(tk.Frame):
    def __init__(self, tkinter, master_view):
        super().__init__(tkinter)
        self.tkinter = tkinter
        self.master_view = master_view
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.master_view.handler_button_clicked
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.tkinter.destroy)
        self.quit.pack(side="bottom")
