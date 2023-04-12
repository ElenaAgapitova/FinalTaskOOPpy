"""Модуль, реализующий класс CommandChange"""
from view.commands.command_abstract import Command


class CommandChange(Command):
    """Данный класс реализует изменение заметки"""

    @property
    def description(self):
        """Возвращает описание команды-метода"""
        return "Изменить заметку"

    def execute(self):
        """Запускает метод изменения заметки"""
        self.console.change_note()
