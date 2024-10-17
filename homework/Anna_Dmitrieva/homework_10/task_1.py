# Задание №1
# Создайте универсальный декоратор, который можно будет
# применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать
# слово "finished"после выполнения декорированной функции.
# Код, использующий этот декоратор может выглядеть, например, так:
#
# @finish_me
# def example(text):
#     print(text)
#
# example('print me')
# В результате работы будет такое:
#
# print me
#
# finished

def my_own_decoration(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("That's all I wanted to write.")
        return result
    return wrapper


@my_own_decoration
def my_text(text):
    print(text)


my_text("Hi, people!")
