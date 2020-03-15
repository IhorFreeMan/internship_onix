# -*- coding: utf-8 -*-
from part_one import FirstClass
import math

class ThreeClass(FirstClass):

    def nok(number_a, number_b):
        """greatest common factor"""
        return print(number_a * number_b // math.gcd(number_a, number_b))

    def nod(number_a, number_b):
        """least common multiple"""
        while number_b != 0:
            number_a, number_b = number_b, number_a % number_b
        return print(number_a)

if __name__ == "__main__":
    t = ThreeClass()
    ThreeClass.nok(4, 5)   # вызов переопределенного статического метода nok
    ThreeClass.nod(4, 5)   # вызов переопределенного статического метода nod

