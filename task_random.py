# -*- coding: utf-8 -*-
from random import (randrange,
                    sample)

def find_random_numer():
    """Find 3 random numbers between 100 and 999 that will be divided by 5"""
    list_random_numer = []
    for i in range(3):
        list_random_numer.append(randrange(100, 999, 5))
    return list_random_numer


def casino():
    """Generate a string of random 10 number
    Generate 100 random lottery tickets (10-digit numbers) and randomly select 2 winning ones"""
    my_dikt = {}
    for i in range(100):
        my_dikt[i] = randrange(1000000000, 1999999999)
    rez = sample(my_dikt.keys(), 2)
    winner_one = rez[0]
    winner_two = rez[1]

    return f"""Первый победитель с билетом  под номером '{winner_one}', с комбинацией '{my_dikt[winner_one]}',
    а также, победил билет под номером '{winner_two}', с комбинацией '{my_dikt[winner_two]}'!"""


if __name__ == "__main__":
    print(find_random_numer())
    print("-----------")
    print(casino())
