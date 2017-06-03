
class Presenter():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.state = self.model.STATE_IDLE

    def process_startpause(self):
        if (self.state == self.model.STATE_IDLE or self.state == self.model.STATE_PAUSED):
            self.state = self.model.STATE_RUNNING
            self.view.set_running_state()
        elif (self.state == self.model.STATE_RUNNING):
            self.state = self.model.STATE_PAUSED
            self.view.set_paused_state()

    def process_stop(self):
        self.state = self.model.STATE_IDLE
        self.view.set_idle_state()

    def run(self):
        self.view.start()
