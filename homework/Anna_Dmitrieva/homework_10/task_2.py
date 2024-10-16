# Создайте универсальный декоратор, который будет
# управлять тем, сколько раз запускается декорируемая функция
#
# Код, использующий этот декоратор может выглядеть, например, так:
# @repeat_me
# def example(text):
#     print(text)
#
#
# example('print me', count=2)
# В результате работы будет такое:
#
# print me
#
# print me
#
# Если есть время и желание погуглить и повозиться,
# то можно попробовать создать декоратор, который сможет обработать такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)
#
# example('print me')

def repeat_decorator(func):

    def wrapper(*args, count, **kwargs):
        for i in range(count):
            func(*args, **kwargs)
    return wrapper


@repeat_decorator
def work_func(text):
    print(text)


work_func("Hi!", count=5)


def repeat_decorator(count=1):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat_decorator(count=6)
def work_func(text):
    print(text)


work_func("Hello!")
