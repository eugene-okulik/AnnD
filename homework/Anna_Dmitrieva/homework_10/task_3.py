# Напишите программу: Есть функция, которая делает
# одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции).
# Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc
# и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из первого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def calc_decoration(func):
    def wrapper(first, second):

        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'

        return func(first, second, operation)

    return wrapper


@calc_decoration
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


number_1 = int(input("Введите первое целое число: "))
number_2 = int(input("Введите второе целое число: "))

result = calc(number_1, number_2)
print(f"Результат: {result}")


# List comprehension
# Дан такой кусок прайс-листа:
#
# (Копируйте эту переменную (константу) в код прямо как есть)
#
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи генераторов превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70,
# 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

price_list = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


dict_price = {item.split()[0]: int(item.split()[1][:-1])
              for item in price_list.splitlines()}

print(dict_price)
