"""Модуль, реализующий класс Validator"""


class Validator:
    """Данный класс обрабатывает пользовательский ввод"""

    def __init__(self):
        self.presenter = None

    @staticmethod
    def get_index(size, text):
        """Возвращает индекс для списка заметок или меню"""
        while True:
            user_input = input(text)
            if (user_input.isdigit() and
                    1 <= int(user_input) <= size):
                index = int(user_input) - 1
                return index
            print(f"\nВведите число от 1 до {size}")
