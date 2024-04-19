# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random


def calculate_total_salary(salary, bonus):
    if bonus:
        bonus_amount = random.randint(0, int(0.2 * salary))
        return salary + bonus_amount
    else:
        return salary


salary = int(input("Введите Вашу зарплату: "))
bonus = random.choice([True, False])

total_salary = calculate_total_salary(salary, bonus)

if bonus:
    print(f"Начислен бонус. Ваша итоговая зарплата составляет: {total_salary}")
else:
    print("Бонус не начислен. Ваша зарплата не изменилась:", total_salary)
