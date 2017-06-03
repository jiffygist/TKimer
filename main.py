from model.model import Model
from view.view import View
from presenter.presenter import Presenter

model = Model()
view = View()
presenter = Presenter(model, view)
view.register_observer(presenter)
presenter.run()