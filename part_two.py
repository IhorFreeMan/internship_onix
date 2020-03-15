# -*- coding: utf-8 -*-
from part_one import FirstClass

class TwoClass(FirstClass):
    def __init__(self, some_variable=None, input__var=None):
        super().__init__(number=None, divisor=None)
        self.some_variable = some_variable
        self.__protected_var = input__var     # защищенная переменная

    def _private_method(self):
        """checks, variable is a string"""
        if type(self.some_variable) is str:
            return print("this is a string")
        else:
            return print(f"{self.some_variable} - not a string")

    def get_private_method(self):
        """displays private method"""
        return self._private_method()

    @property
    def protected_var(self):
        """getter protected_var"""
        return print(self.__protected_var)

    @protected_var.setter
    def protected_var(self, input__var):
        """setter protected_var"""
        self.__protected_var = input__var


if __name__ == "__main__":
    t = TwoClass()                    # создавать экземпляр класса
    t.number = 2                      # присвоить значение переменной определённой в классе родителе FirstClass
    t.divisor = 2                     # присвоить значение переменной определённой в классе родителе FirstClass
    t.is_divisible_by()               # вызов метода is_divisible_by который определен в классе FirstClass
    t.some_variable = 7               # присвоить значение
    t.get_private_method()            # вызвать приватный метод

    t.protected_var = 'protected'     # присвоить значение protected_var
    t.protected_var                   # вызвать защищенный метод
    print(t._TwoClass__protected_var) # вызвать защищенный метод




