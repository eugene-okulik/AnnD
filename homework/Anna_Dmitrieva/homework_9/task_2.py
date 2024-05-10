# Map, filter
# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34,
# 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого
# писка новый список с жаркими днями. Будем считать жарким всё, что выше 28.
# Распечатайте из новeooого списка самую высокую температуру
# самую низкую и среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30,
                29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31,
                30, 32, 30, 28, 24, 23]


new_list_temper = filter(lambda x: x > 28, temperatures)
new_list_temper = list(new_list_temper)
temperature_max = max(new_list_temper)
temperature_min = min(new_list_temper)
temperature_avg = round(sum(new_list_temper) / len(new_list_temper), 1)

print('Самая высокая температура -', temperature_max)
print('Самая низкая температура -', temperature_min)
print('Средняя температура -', temperature_avg)
