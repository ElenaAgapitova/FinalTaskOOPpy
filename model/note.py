""" Модуль, реализующий класс для создания заметок и для работы с ними. """
from datetime import datetime


class Note:
    """
        Класс для создания заметки.

        Атрибуты:
        __text_note (str): текст заметки.
        __creation_data (str): дата/время создания заметки.
        __changes_data (str): дата/время последнего изменения заметки
        Методы:
        1. get_creation_data: возвращает дату и время создания заметки.
        2. get_changes_data: возвращает дату и время последнего изменения заметки.
        3. get_text_note: возвращает текст-содержание заметки.
        4. change: изменение заметки.
    """

    def __init__(self, title, creation_data, text_note, changes_data=''):
        self.__title = title
        self.__text_note = text_note
        self.__creation_data = creation_data
        self.__changes_data = changes_data

    def get_title(self):
        return self.__title

    def get_creation_data(self):
        """
        Возвращает дату и время создания заметки.
        :return: дата и время создания заметки.
        """
        return self.__creation_data

    def get_changes_data(self):
        """
        Возвращает дату и время последнего изменения заметки.
        :return: дата и время последнего изменения заметки.
        """
        return self.__changes_data

    def get_text_note(self):
        """
        Возвращает текст заметки.
        :return: текст-содержание заметки.
        """
        return self.__text_note

    def change(self, new_text: str):
        """
        Изменение текста и даты/время заметки.
        :param new_text: текст заметки.
        """
        self.__text_note = new_text
        self.__changes_data = datetime.today().strftime('%d.%m.%Y %H:%M')
