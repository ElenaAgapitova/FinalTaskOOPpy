"""Модуль, реализующий класс FileReader (чтение и запись данных в файл в формате csv"""
import csv

from model.note import Note
from model.notebook import Notebook


class FileReader:
    """Данный класс реализует чтение заметок из файла и запись в файл в формате csv"""

    def __init__(self, path: str):
        self.path = path

    def file_read(self, notebook: Notebook):
        """Чтение заметок из файла"""
        try:
            with open(self.path, 'r', encoding='1251') as data:
                reader = csv.reader(data, delimiter=';')
                for i, note_list in enumerate(reader):
                    if i:
                        notebook.get_notes().append(Note(note_list[1], note_list[3], note_list[2],
                                                         note_list[4]))
        except FileNotFoundError:
            pass
        return notebook

    def save_changes(self, notebook: Notebook):
        """Запись заметок в файл"""
        with open(self.path, 'w', encoding='1251', newline='') as data:
            writer = csv.writer(data, delimiter=';')
            writer.writerow(['№', 'Заголовок', 'Заметка', 'Дата/время создания',
                             'Дата/время изменения'])
            for i, note in enumerate(notebook.get_notes(), start=1):
                writer.writerow([i, note.get_title(), note.get_text_note(),
                                 note.get_creation_data(), note.get_changes_data()])
