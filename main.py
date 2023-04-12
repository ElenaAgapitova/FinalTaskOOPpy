"""Основной модуль запуска программы"""

from model.notebook import Notebook
from presenter.presenter import Presenter
from view.console import Console

if __name__ == '__main__':
    model = Notebook()
    view = Console()
    presenter = Presenter(view, model, 'notes.csv')
    view.start()




