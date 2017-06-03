
class Presenter():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process_button_clicked(self):
        print("hi there, everyone!")

    def run(self):
        self.view.start()
