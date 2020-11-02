"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

some_list = [1, 2, 3, None, True, 'text', [1, 2, 3], (1, 2, 3), {1, 2, 3}]
print(type(some_list[1]))
print(type(some_list[3]))
print(type(some_list[4]))
print(type(some_list[5]))
print(type(some_list[6]))
print(type(some_list[7]))
print(type(some_list[8]))
