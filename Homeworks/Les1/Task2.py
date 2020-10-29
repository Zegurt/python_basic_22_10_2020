"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time_user = int(input("Введите время в секундах: \n>>>"))
time_hours = time_user // 3600
time_minutes = (time_user - time_hours * 3600) // 60
time_second = time_user - (time_hours * 3600 + time_minutes * 60)
print(f"Точное время  {time_hours} ч. : {time_minutes}  мин. : {time_second} сек.")
