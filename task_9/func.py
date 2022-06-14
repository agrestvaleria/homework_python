# Написать калькулятор.
# Программа должна содержать 4 функции принимающие два аргумента
# и возвращающие результаты сложения, вычитания, умножения и деления.
# Реализовать пользовательский интерфейс Methods. От него унаследовать математические методы и реализовать их.
# Добавить валидацию входных данных. Программа должна состоять из двух файлов(main.py, func.py).

from abc import ABC, abstractmethod


class CalculatorMethods(ABC):

    @abstractmethod
    def sum(self, x, y):
        pass

    @abstractmethod
    def deduction(self, x, y):
        pass

    @abstractmethod
    def multiplication(self, x, y):
        pass

    @abstractmethod
    def division(self, x, y):
        pass
