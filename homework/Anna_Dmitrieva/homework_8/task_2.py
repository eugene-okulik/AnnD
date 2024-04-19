# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число,
# тысячное число, стотысячное число

def fibonacci_series():
    indexes = [5, 200, 1000, 100000]
    index = 0
    fib1, fib2 = 0, 1
    while index < 100000:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
        if index in indexes:
            print(fib2)
        index += 1


for number in fibonacci_series():
    pass
