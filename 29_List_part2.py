'''
Удаление элементов списка
'''

mushrooms = ['lisichki', 'volnushki', 'opyata', 'belye', 'gruzdi', 'gruzdi', 'syroezhki', 'podosinoviki', 'podberezoviki']
mushrooms.remove('gruzdi') # если элментов в списке несколько, то удаляется первый по списку элемент
print(mushrooms)
print('---------')
del mushrooms[4]
print(mushrooms)
print('---------')
if 'belye' in mushrooms:
    print('belye in list')
if 'maslyata' not in mushrooms:
    print('masltyata not found in list')
print('---------')
mushrooms = ['lisichki', 'volnushki', 'opyata', 'belye', 'gruzdi', 'gruzdi']
print(mushrooms.index('gruzdi')) # тоже отображает индекс первого найденного элемента в списке
#print(mushrooms.index('maslyata')) # тут будет ошибка, так как такого элемента в списке нет
print('---------')
'''
Сортировка списков
'''
mushrooms = ['lisichki', 'volnushki', 'opyata', 'belye', 'gruzdi', 'syroezhki', 'podosinoviki', 'podberezoviki']
print(sorted(mushrooms))
print('---------')
mushrooms.sort()
print(mushrooms)
print('---------')
print(min(mushrooms))
print(max(mushrooms))
print('---------')
mushrooms.reverse()
print(mushrooms)
print('---------')
print(list(reversed(mushrooms)))
'''
Функция reversed() возвращает не список, а итератор, и если нужно дальше использовать именно список,
то результат придется сначала в него сконвертировать. И нужно знать, как минимум, что итератор вещь одноразовая,
он позволяет только один раз перебрать элементы последовательности, для которой создан. Например:
mylist = [1, 2, 3]
reversed_list = reversed(mylist)
for el in reversed_list:
    print(el)
new_list = list(reversed_list)
в последней строке будет присвоен пустой лист,
т.к. итератор исчерпал себя в цикле и дальше будет возвращать только пустые элементы.
Поэтому, если нужно получить новый развернутый список,
то нужно писать new_list = list(reversed(old_list)) - т.е. сразу преобразовать итератор в список.
'''
print('---------')
print(mushrooms[::-1])