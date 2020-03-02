# -*- coding: utf-8 -*-

""" 1. Создать числовую переменную"""
numeric_variable = int()
print(f"Тип переменной 'numeric_variable' == {type(numeric_variable)}")

""" 2. создать переменную с типом строка """
string_variable = str()
print(f"Тип переменной 'string_variable' == {type(string_variable)}")

""" 3. сравнить их типы """
compare_types = type(numeric_variable) != type(string_variable)
print(compare_types)

""" 4. конвертировать числовую переменную в строчную"""
numeric_variable = str(numeric_variable)

print(f"Тип переменной 'numeric_variable' == {type(numeric_variable)}")

""" 5. Создать список"""
my_list = list()
print(f"Тип переменной 'my_list' == {type(my_list)}")

""" 6. добавить элемент в конец списка """
my_list.append('some element')
print(my_list)


""" 7. добавить элемент в нужную позицию в списке"""
my_list.insert(0, 'next variable')
print(f'Добавить элемент в индекс {my_list.index("next variable")} .')

""" 8. удалить первый элемент"""
my_list.remove("next variable")
print(my_list)

""" 9. удалить элемент списка по индексу"""
my_list.pop(0)
print(my_list)

""" 10. развернуть список"""
my_list = list([1, 2, 3, 4, 5])
my_list.reverse()
print(my_list)

""" 11. подсчитать количество элементов в списке"""
len_my_list = len(my_list)
print(len_my_list)

""" 12. Сделать копию списка """
copy_my_list = my_list.copy()
print(copy_my_list)

""" 13. Сортировать первый список одним из алгоритмов сортировки """
def bubble_sort(items):
    lst = list(items)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

print(bubble_sort(copy_my_list))

""" 14. Сортировать второй список одним из стандартных методов """
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

""" 16. Отсортировать строку по алфавиту ”This is a test string for Internship Onix for python“  """
my_string = "This is a test string for Internship Onix for python"

def my_sort(my_str):
        sort_list = sorted(my_str.split(), key=str.lower)
        sort_str = ' '
        return sort_str.join(sort_list)

print(my_sort(my_string))

""" 17. Создать словарь"""
variable_dictionary = dict()
print(f"Тип переменной 'variable_dictionary' == {type(variable_dictionary)}")

""" 18. добавить элемент в словарь """
variable_dictionary['my_key'] = 'my_value'

""" 19. получить значение из словаря по ключу"""
print(variable_dictionary.get('my_key'))

""" 20. удалить элемент из словаря """
del variable_dictionary['my_key']

""" 21. получить все ключи"""
variable_dictionary = {
    'key_one': 1,
    'key_two': 2,
    'key_three': 3,
    'key_four': 4,
    'key_five': 5,
}

for my_keys in variable_dictionary.keys():
    print(my_keys)

""" 22. получить все значения """
for my_values in variable_dictionary.values():
    print(my_values)

""" 23. Сортировать словарь по ключам """
for key in sorted(variable_dictionary, key=str.lower):
    print(key, variable_dictionary[key])


""" 24. Сортировать словарь по значениям """
for key in sorted(variable_dictionary,  key=variable_dictionary.get):
    print(key, variable_dictionary[key])

