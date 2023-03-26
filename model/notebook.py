"""Модуль, реализующий класс для создания записной книжки и работы с ней"""

from model.note import Note


class Notebook:
    """
    Класс для создания записной книжки.

        Атрибуты:
        __notes (list): список заметок.

        Методы:
        1. __str__: возвращает строковое представление записной книжки.
        2. add: добавить новую заметку в записную книжку.
        3. size: получить длину списка.
        4. remove: удалить заметку из списка.
        5. change_note: изменить заметку.
        6. is_full: проверить заполнена ли записная книжка
    """

    def __init__(self):
        self.__notes = []

    def size(self):
        """Возвращает длину записной книжки"""
        return len(self.__notes)

    def add(self, text_note):
        """Добавить заметку в записную книжку"""
        note = Note(text_note)
        self.__notes.append(note)

    def remove(self, index):
        """Удалить заметку из книжки"""
        del self.__notes[index]

    def change_note(self, index, update_text):
        """Изменить заметку в книжке"""
        self.__notes[index].change_text(update_text)

    def __str__(self):
        """Данный метод возвращает строковое представление заметки"""
        notes_string = "\nСписок заметок:\n"
        for i, note in enumerate(self.__notes, start=1):
            notes_string += f"\t{i}. {note}\n"
        return notes_string

    def is_full(self):
        """Возвращает True, если в записной книжке есть записи"""
        return bool(self.__notes)
