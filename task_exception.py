# -*- coding: utf-8 -*-

def my_exception(spirits):
    """create your own exception"""
    try:
        if spirits == 'Bad':
            raise TypeError()
    except TypeError:
        print("Поймано исключение TypeError")

def my_exception_two(spirits):
    """call an exception"""
    if spirits == 'Ok':
        raise TypeError("Описание исключения")
    else:
        print("everything is good")

def my_exception_three(div1, div2):
    """exception handling division by zero"""
    try:
        print(div1 / div2)
    except ZeroDivisionError as v:
        print("Описание исключения")
        # raise
        print(v)

class MyError(Exception):
    pass

def my_exception_four(spirits):
    """create your own exception type"""
    try:
        if spirits == 'Ok':
            raise MyError("create your own exception type")
    except MyError as er:
        print(er)
    finally:
        print("End-")


if __name__ == "__main__":
    my_exception('Bad')
    print("------------")
    my_exception_two('Bad')
    # my_exception_two('Ok')
    print("------------")
    my_exception_three(3, 0)
    print("------------")
    print(my_exception_four('Ok'))
