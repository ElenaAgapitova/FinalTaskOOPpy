"""Модуль класса CommandExit"""
from view.commands.command_abstract import Command


class CommandExit(Command):
    """Класс CommandExit позволяет завершить работу программы."""

    @property
    def description(self):
        """Возвращает описание команды для вывода в меню."""
        return "Завершить работу"

    def execute(self):
        """Вызывает метод, которые завершает работу программы"""
        self.console.finish()
