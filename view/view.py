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

    # Widget interaction handlers

    def handler_button_clicked(self):
        self.presenter.process_button_clicked()




