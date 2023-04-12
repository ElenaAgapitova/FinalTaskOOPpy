"""Модуль, реализующий класс для создания записной книжки и работы с ней"""
from datetime import datetime

from tabulate import tabulate

from model.note import Note


class Notebook:
    """
    Класс для создания записной книжки.

        Атрибуты:
        __notes (list): список заметок.

        Методы и свойства:
        1. get_notes: возвращает список заметок.
        2. add_note: добавить новую заметку в записную книжку.
        3. size: получить длину списка заметок.
        4. remove_note: удалить заметку из списка.
        5. change_note: изменить заметку.
        6. is_full: проверить заполнена ли записная книжка.
        7. tabl: возвращает содержание записной книжки в виде таблицы.
    """

    def __init__(self):
        self.__notes = []

    def size(self):
        """Возвращает длину записной книжки"""
        return len(self.__notes)

    def add_note(self, title, text_note):
        """Добавить заметку в записную книжку"""
        note = Note(title, datetime.today().strftime('%d.%m.%Y %H:%M'), text_note)
        self.__notes.append(note)

    def remove_note(self, index):
        """Удалить заметку из книжки"""
        del self.__notes[index]

    def change_note(self, index, title, update_text):
        """Изменить заметку в книжке"""
        self.__notes[index].change(title, update_text)

    def is_full(self):
        """Возвращает True, если в записной книжке есть записи"""
        return bool(self.__notes)

    def get_notes(self):
        """Возвращает список заметок"""
        return self.__notes

    @property
    def tabl(self):
        """
        Формирует представление записной книжки в виде таблицы.
        :return: таблицу заметок.
        """
        headers = ['№', 'Заголовок', 'Заметка', 'Дата/время создания', 'Дата/время изменения']
        tabl = [[i, note.get_title(), note.get_text_note(),
                 note.get_creation_data(), note.get_changes_data()]
                for i, note in enumerate(self.__notes, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')

    def filter_by_date(self, date):
        """
        Фильтрует заметки по дате, формирует представление записной книжки в виде таблицы.
        :param date: дата, по которой необходимо сделать выборку заметок.
        :return: таблицу заметок.
        """
        headers = ['№', 'Заголовок', 'Заметка', 'Дата/время создания', 'Дата/время изменения']
        tabl = [[i, note.get_title(), note.get_text_note(), note.get_creation_data(),
                 note.get_changes_data()] for i, note in enumerate(self.__notes, start=1)
                if date in note.get_creation_data() or date in note.get_changes_data()]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')
