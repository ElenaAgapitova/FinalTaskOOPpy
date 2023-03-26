""" Модуль, реализующий класс для создания заметок и для работы с ними. """
from datetime import datetime


class Note:
    """
        Класс для создания заметок.

        Атрибуты:
        __text_note (str): текст заметки.
        __data (datetime): дата создания заметки.

        Методы:
        1. __str__: возвращает строковое представление заметки.
        2. change_text: изменить текст заметки.
    """

    def __init__(self, text_note, data=datetime.today().strftime('%d.%m.%Y')):
        self.__text_note = text_note
        self.__data = data

    def __str__(self):
        """Данный метод возвращает строковое представление заметки"""
        return f"{self.__data} {self.__text_note}"

    def change_text(self, new_text: str):
        """Изменить текст заметки"""
        self.__text_note = new_text
