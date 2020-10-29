"""
Поработайте с переменными, создайте несколько, выведите на экран/
Запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

string_variable = "Hello world"  # переменнаяв строке
print(string_variable)  # выведение на экран

int_variable = 5
print(int_variable)

float_variable = 12.2
print(float_variable)

greetings = "Заполнение анкеты"
print(greetings)
user_name = input("Введите ваше имя\n>>>")
user_age = input("Введите ваш возраст\n>>>")
user_height = input("Введите ваш рост\n>>>")
print("Ваши данные: Имя: {0}. Возраст: {1}. Рост: {2}".format(user_name, user_age, user_height))


