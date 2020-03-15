# -*- coding: utf-8 -*-
class FirstClass():
    def __init__(self, number=None, divisor=None):
        """Constructor"""
        self.number = number
        self.divisor = divisor

    def __del__(self):
        """destructor"""
        return print('--object deleted--')

    def is_divisible_by(self):
        """ function is_divisible_by (number, divisor),
        checks if the number divides the number
        without a remainder by the divisor"""
        return print(self.number % self.divisor == 0)

    @staticmethod
    def multiply(number_a, number_b):
        """multiply a and b"""
        print((lambda a, b: a * b)(number_a, number_b))

    @staticmethod
    def nod(self):
        """greatest common factor"""
        pass

    @staticmethod
    def nok(self):
        """least common multiple"""
        pass

if __name__ == "__main__":
    c = FirstClass()          # создавать экземпляр класса
    c.number = 4              # присвоить значение
    c.divisor = 5
    c.is_divisible_by()       # вызов метода is_divisible_by()
    del c                     # удаление экземпляра
    FirstClass.multiply(2, 2) # вызов статического метода




