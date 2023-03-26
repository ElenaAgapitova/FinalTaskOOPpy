"""Модуль для взаимодействия с пользователем (консоль)"""
from view.commands.menu import Menu
from view.validator import Validator
from view.view_abstract import View


class Console(View):
    """Данный класс реализует взаимодействие с пользователем (консоль)"""
    __working = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        """Устанавливает объект презентера в консоли."""
        self.presenter = presenter

    def show_all(self):
        """Вывод всех заметок в консоль"""
        if self.presenter.is_full():
            print(self.presenter.get_notebook())
        else:
            print("\nВ записной книжке нет заметок!")

    def remove_note(self):
        """Метод для удаления заметки по номеру"""
        if self.presenter.is_full():
            index = Validator.get_index(self.presenter.get_size_notebook(),
                                        "\nВведите номер заметки: ")
            self.presenter.remove_note(index)
            print("\nЗаметка удалена!\n")
        else:
            print("\nВ записной книжке нет заметок!")

    def change_note(self):
        """Метод для изменения заметки по индексу"""
        if self.presenter.is_full():
            index = Validator.get_index(self.presenter.get_size_notebook(),
                                        "\nВведите номер заметки: ")
            update_note = input("\nОбновите заметку: ")
            self.presenter.change_note(index, update_note)
            print("\nЗаметка изменена!\n")
        else:
            print("\nВ записной книжке нет заметок!")

    def add_note(self):
        """Метод для добавления новой заметки"""
        new_note = input("\nВведите заметку: ")
        self.presenter.add_note(new_note)
        print("\nЗаметка добавлена!\n")

    def finish(self):
        """Завершение работы программы"""
        self.__working = False
        print("\nЗавершение работы...")

    def start(self):
        """
        Начинает работу консоли, показывая меню и выполняя выбранные пользователем действия.
        Запрашивает у пользователя ввод, пока работа консоли не завершится.
        """
        self.__working = True
        menu = Menu(self)
        while self.__working:
            print(menu)
            index = Validator.get_index(menu.get_size_menu(), "\nВыберите пункт меню: ")
            menu.execute(index)
