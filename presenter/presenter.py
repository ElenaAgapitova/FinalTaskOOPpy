"""Модуль, реализующий класс Presenter"""


class Presenter:
    """
    Presenter для паттерна MVP.
    Принимает на вход экземпляры View и Notebook и связывает их между собой.
    """

    def __init__(self, view, notebook):
        self.__view = view
        self.__notebook = notebook
        self.__view.set_presenter(self)

    def is_full(self):
        """
            Проверяет, заполнена ли записная книжка.
            :return: True, если записная книжка заполнена, и False в противном случае.
        """
        return self.__notebook.is_full()

    def add_note(self, text_note):
        """Добавляет новую запись в записную книжку."""
        self.__notebook.add(text_note)

    def remove_note(self, index):
        """Удаляет запись в записной книжке по указанному индексу."""
        self.__notebook.remove(index)

    def change_note(self, index, update_text):
        """Обновляет текст заметки в записной книжке"""
        self.__notebook.change_note(index, update_text)

    def get_size_notebook(self):
        """Возвращает размер записной книжки"""
        return self.__notebook.size()

    def get_notebook(self):
        """Возвращает строковое представление записной книжки"""
        return self.__notebook
