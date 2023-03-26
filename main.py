"""Основной модуль запуска программы"""

from model.notebook import Notebook
from presenter.presenter import Presenter
from view.console import Console

if __name__ == '__main__':
    model = Notebook()
    model.add("первая заметка")
    model.add("вторая заметка")

    view = Console()
    presenter = Presenter(view, model)
    view.start()
