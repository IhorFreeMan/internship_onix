# -*- coding: utf-8 -*-
from random import (randrange,
                    choice,
                    shuffle)

def find_random_number():
    """Find 3 random numbers between 100 and 999 that will be divided by 5"""
    m = []
    while True:
        if len(m)<3:
            my_random = randrange(100, 999)
            if my_random % 5 == 0:
                m.append(my_random)
        else:
            return m

# Generate a string of random 10 number
def random_characters():
    str1 = ''
    for i in range(10):
        m = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        shuffle(m)
        str1 += ''.join(choice(m))
    return str1

# Generate 100 random lottery tickets (10-digit numbers) and randomly select 2 winning ones
def casino():
    my_dict = {}
    # Generate 100 random lottery tickets
    for i in range(1, 101):
        my_dict[i] = random_characters()
    # randomly select 2 winning
    winni_one = randrange(1, 100)
    winni_two = randrange(1, 100)
    return f"""Первый победитель с билетом  под номером '{winni_one}', с комбинацией '{my_dict[winni_one]}',
    а также, победил билетом под номером '{winni_two}', с комбинацией '{my_dict[winni_two]}'!"""


if __name__ == "__main__":
    print(find_random_number())
    print("-----------")
    # print(random_characters())
    print(casino())
