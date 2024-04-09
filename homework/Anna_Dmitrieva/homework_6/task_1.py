# Напишите программу, которая добавляет ‘ing’
# к словам (к каждому слову) в тексте “Etiam tincidunt
# neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero” и после этого выводит
# получившийся текст на экран. Знаки препинания
# не должны оказаться внутри слова.
# Если после слова идет запятая или точка,
# этот знак препинания должен идти
# после того же слова, но уже преобразованного.

text = ('tiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
safe_words = []

for word in words:
    if word.endswith(('.', ',')):
        word_with_add = word[:-1] + 'ing' + word[-1]
    else:
        word_with_add = word + 'ing'
    safe_words.append(word_with_add)

print(' '.join(safe_words))
