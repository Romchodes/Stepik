'''
Перебор элементов словаря (dictionary)
'''
d = {'C': 7, 'A': 5, 'T': 3, 'G': 9}
for key in d:
    print(key, end = ' ')
print('\n---------')
for key in d.keys():
    print(key, end = ' ')
print('\n---------')
for value in d.values():
    print(value, end = ' ')
print('\n---------')
for key, value in d.items():
    print(key, value, end = '; ')
print('\n---------')

'''
Посмотрим сколько будет "весить" словарь, множество, список, кортеж и генератор размером на 100 элементов.

Для определения размера использовал import sys и sys.getsizeof(...)

type - <class 'dict'>, len - 100, size - 2620         #   {i:i for i in range(100)}
type - <class 'set'>, len - 100, size - 4212          #   {i for i in range(100)}
type - <class 'list'>, len - 100, size - 460            #   [i for i in range(100)]
type - <class 'tuple'>, len - 100, size - 428         #   tuple((i for i in range(100)))
type - <class 'generator'>, len - 100, size - 48   #   (i for i in range(100))

Все приведённые размеры указаны в байтах.
'''
d = {'a333aa13': ['Иванов', 'Петров', 'Александров']}
print(d['a333aa13'])