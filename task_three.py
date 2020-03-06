# -*- coding: utf-8 -*-
import my_decorator

@my_decorator.start_and_end_function
def mix_of_tasks():
    """ 1. In this function tasks from task two """

    """ 1. Create a numeric variable """
    numeric_variable = int()
    print(f"Тип переменной 'numeric_variable' == {type(numeric_variable)}")

    """ 2. create a variable of type string """
    string_variable = str()
    print(f"Тип переменной 'string_variable' == {type(string_variable)}")

    """ 3. compare their types """
    compare_types = type(numeric_variable) != type(string_variable)
    print(compare_types)

    """ 4. convert numeric variable to string """
    numeric_variable = str(numeric_variable)

    print(f"Тип переменной 'numeric_variable' == {type(numeric_variable)}")

    """ 5. Create a list """
    my_list = list()
    print(f"Тип переменной 'my_list' == {type(my_list)}")

    """ 6. add item to end of list """
    my_list.append('some element')
    print(my_list)


    """ 7. add an item to the desired position in the list"""
    my_list.insert(0, 'next variable')
    print(f'Добавить элемент в индекс {my_list.index("next variable")} .')

    """ 8. delete first element """
    my_list.remove("next variable")
    print(my_list)

    """ 9. remove list item by index """
    my_list.pop(0)
    print(my_list)

    """ 10. reverse list """
    my_list = list([1, 2, 3, 4, 5])
    my_list.reverse()
    print(my_list)

    """ 11. count the number of items in a list """
    len_my_list = len(my_list)
    print(len_my_list)

    """ 12. Make a copy of the list """
    copy_my_list = my_list.copy()
    print(copy_my_list)

    """ 13. Sort the first list using one of the sorting algorithms """
    def bubble_sort(items):
        lst = list(items)
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[j] < lst[i]:
                    lst[j], lst[i] = lst[i], lst[j]
        return lst

    print(bubble_sort(copy_my_list))

    """ 14. Sort the second list using one of the standard methods """
    my_list.sort()
    print(my_list)

    """ 15.  Чем отличается .sort() от sorted() """
    """
    метод sort() не возвращает новую отсортированную 
    копию списка, а обновляет список с измененным порядком
    элементов (my_list.sort())
    
    Функция sorted работает с любой последовательностью и возвращает
    новый список с упорядоченными элементами (sorted(my_list))
    """

    """ 16. Sort string alphabetically ”This is a test string for Internship Onix for python“  """
    my_string = "This is a test string for Internship Onix for python"

    def my_sort(my_str):
            sort_list = sorted(my_str.split(), key=str.lower)
            sort_str = ' '
            return sort_str.join(sort_list)

    print(my_sort(my_string))

    """ 17. Create dictionary """
    variable_dictionary = dict()
    print(f"Тип переменной 'variable_dictionary' == {type(variable_dictionary)}")

    """ 18. add item to dictionary """
    variable_dictionary['my_key'] = 'my_value'

    """ 19. get the value from the dictionary by key """
    print(variable_dictionary.get('my_key'))

    """ 20. remove item from dictionary """
    del variable_dictionary['my_key']

    """ 21. get all keys """
    variable_dictionary = {
        'key_one': 1,
        'key_two': 2,
        'key_three': 3,
        'key_four': 4,
        'key_five': 5,
    }

    for my_keys in variable_dictionary.keys():
        print(my_keys)

    """ 22. get all values  """
    for my_values in variable_dictionary.values():
        print(my_values)

    """ 23. Sort dictionary by key """
    for key in sorted(variable_dictionary, key=str.lower):
        print(key, variable_dictionary[key])


    """ 24. Sort dictionary by values """
    for key in sorted(variable_dictionary,  key=variable_dictionary.get):
        print(key, variable_dictionary[key])


""" 2. Create a global variable """
my_global_variable = 3

@my_decorator.start_and_end_function
def function_multiply(numeric=0):
    """
    3. Create a function that will take in
    yourself a numerical variable, multiply it by global and write
    to the list, and return the list and the number of elements in it
    """
    my_list =[]
    my_list.append(numeric * my_global_variable)
    return print(my_list, len(my_list))

@my_decorator.start_and_end_function
def take_function(*args, **kwargs):
    """4. Create a function that takes in *args, **kwargs"""
    return print(args, kwargs)

@my_decorator.start_and_end_function
def is_divisible_by(num, divisor):
    """ 5. function is_divisible_by (number, divisor), checks if the number divides the number without a remainder by the divisor"""
    return print(num % divisor==0)


def my_fib(rabbit):
    """6. The function will count the fibonacci numbers"""
    if rabbit in (1, 2):
        return 1
    return my_fib(rabbit - 1) + my_fib(rabbit - 2)


if __name__ == "__main__":
    mix_of_tasks()
    function_multiply(5)
    take_function(1, 2, 3, 4, r=7, g=6)
    is_divisible_by(3, 3)
    print('Start is_my_fib')
    for rabbit in range(1, 10):
        print(my_fib(rabbit), end=" ")
    print('\n', '-end my_fib-')





