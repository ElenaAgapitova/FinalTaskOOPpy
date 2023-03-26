"""Модуль, реализующий класс Menu"""

from view.commands.command_add import CommandAdd
from view.commands.command_change import CommandChange
from view.commands.command_exit import CommandExit
from view.commands.command_remove import CommandRemove
from view.commands.command_show_all import CommandShowAll


class Menu:
    """Данный класс создает основное меню и реализует запуск методов"""

    def __init__(self, console):
        self.commands = []
        self.commands.append(CommandShowAll(console))
        self.commands.append(CommandAdd(console))
        self.commands.append(CommandChange(console))
        self.commands.append(CommandRemove(console))
        self.commands.append(CommandExit(console))

    def __str__(self):
        """Возвращает строковое представление меню"""
        menu_string = "\n======== Главное меню ========\n"
        for i, cmd in enumerate(self.commands, start=1):
            menu_string += f"\t{i}. {cmd.description}\n"
        return menu_string

    def get_size_menu(self):
        """Возвращает длину списка меню"""
        return len(self.commands)

    def execute(self, index):
        """Запускает метод в зависимости от выбора пользователя по индексу команды в списке"""
        option = self.commands[index]
        option.execute()
