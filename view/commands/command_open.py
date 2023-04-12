"""Модуль, реализующий класс CommandOpen"""
from view.commands.command_abstract import Command


class CommandOpen(Command):
    """Данный класс реализует выполнения команды - заполнение записной книжки из файла"""


    @property
    def description(self):
        """Возвращает описание команды"""
        return "Открыть записную книжку"

    def execute(self):
        """Запускает команду заполнения записной книжки из файла"""
        self.console.open_notebook()
