# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова”
# и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа
# пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
#
# Подсказка: задание выполняется с помощью цикла while

programms_number = '4'

while True:
    number_from_user = input("Поиграем? Попробуй угадать задуманную "
                             "мной цифру:  ")

    if not number_from_user.isdigit():
        print("Не шути так, введи цифру!")
        continue

    if number_from_user != programms_number:
        print("Ну, конечно, мимо! Попробуй снова!")
        continue
    else:
        print('Поздравляю! Вы угадали!')
        print('Приходи еще!')
        break
