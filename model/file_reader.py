"""Модуль, реализующий класс FileReader (чтение и запись данных в файл в формате txt"""
from model.note import Note
from model.notebook import Notebook


class FileReader:
    """Данный класс реализует чтение заметок из файла и запись в файл"""

    def __init__(self, path: str):
        self.path = path

    def file_read(self, notebook: Notebook):
        """Чтение заметок из файла"""
        try:
            with open(self.path, 'r', encoding='UTF-8') as data:
                notes = data.readlines()
                for note in notes:
                    note_list = note.strip().replace(' ', '§', 1).split('§')
                    notebook.get_notes().append(Note(note_list[0], note_list[1]))
        except FileNotFoundError:
            pass
        return notebook

    def save_changes(self, notebook: Notebook):
        """Запись заметок в файл"""
        with open(self.path, 'w', encoding='UTF-8') as data:
            for note in notebook.get_notes():
                data.write(str(note) + '\n')
