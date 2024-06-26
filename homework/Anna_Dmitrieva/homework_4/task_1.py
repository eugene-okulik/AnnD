# Создайте словарь (и сохраните его в переменную my_dict) с
# такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.

my_dict = {'tuple': (5, 4, 3, 2, 1),
           'list': [1, 2, 3, 4, 5],
           'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
           'set': {6, 7, 8, 9, 1}}

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент

print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент

my_dict['list'].append(6)

# удалите второй элемент списка
my_dict['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением

my_dict['dict'][('i am a tuple',)] = 'did not like tuple'

# удалите какой-нибудь элемент

my_dict['dict'].pop('e')

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество

my_dict['set'].add('bingo')

# удалите элемент из множества

my_dict['set'].remove(6)

# В конце выведите на экран весь словарь

print(my_dict)
