"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

some_list = []
some_element1 = int(input('Введите 1 число списка\n>>>'))
some_list.add(some_element1)
some_element2 = int(input('Введите 2 число списка\n>>>'))
some_list.add(some_element2)
some_element3 = int(input('Введите 3 число списка\n>>>'))
some_list.add(some_element3)
some_element4 = int(input('Введите 4 число списка\n>>>'))
some_list.add(some_element4)
some_element5 = int(input('Введите 5 число списка\n>>>'))
some_list.add(some_element5)


"""
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)
"""
