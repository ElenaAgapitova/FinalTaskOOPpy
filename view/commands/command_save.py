"""Модуль, реализующий команду CommandSave"""
from view.commands.command_abstract import Command


class CommandSave(Command):
    """Данный класс реализует выполнения команды - сохранение изменений в записной книжке в файл"""

    @property
    def description(self):
        """Возвращает описание команды"""
        return "Сохранить изменения"

    def execute(self):
        """Запускает команду сохранение и записи заметок в файл"""
        self.console.save_changes()
