"""Модуль реализующий класс CommandAdd (добавление заметки)"""
from view.commands.command_abstract import Command


class CommandAdd(Command):
    """Класс реализует добавление заметки"""

    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        """Возвращает описание команды"""
        return "Добавить заметку"

    def execute(self):
        """Запускает метод добавления заметки"""
        self.console.add_note()
