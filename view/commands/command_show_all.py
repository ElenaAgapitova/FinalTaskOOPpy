"""Модуль, реализующий класс CommandShowAll"""
from view.commands.command_abstract import Command


class CommandShowAll(Command):
    """Данный класс реализует метода вывода всех заметок в консоль"""

    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        """Возвращает описание команды-метода"""
        return "Показать все заметки"

    def execute(self):
        """Запускает метод вывода заметок в консоль"""
        self.console.show_all()
