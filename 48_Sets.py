'''
Множества (set)
Изменяемые
Элементы не имеют порядка
List - Список. Элементы в списке хранятся последовательно, каждому из них присвоены индексы, начиная с нуля.
Tuple - Кортеж, неизменяемый и более быстрый аналог списка.
Set - Множество, набор уникальных элементов в случайном порядке (неупорядоченный список).
'''

s = set() # создание пустого множества
basket = {'butter', 'bread', 'milk', 'meat', 'fish', 'tea', 'water', 'water', 'water'}
print(len(basket)) # дублирующиеся элементы не учитываются
print(basket) # элементы множества выводятся в случайном порядке и при наличии дублей - выводится только один элемент
print('tea' in basket)
print('cola' in basket)
'''
Операции со множествами
'''
print('---------')
basket.add('noodles')
print(basket)
print('---------')
basket.add('tea') # если добавить уже имеющийся элемент, то множество не изменится
print(basket)
print('---------')
basket.remove('water')
print(basket)
print('---------')
# basket.remove('lemon') # будет ошибка, так как такого элемента нет во множестве
# print(basket)
# print('---------')
basket.discard('lemon') # удаление элемента, даже если такого элемента нет, то ошибки не будет
print(basket)
print('---------')
basket.discard('butter')
print(basket)
print('---------')
print(len(basket))
print('---------')
basket.clear()
print(basket)
print('---------')
basket = {'butter', 'bread', 'milk', 'meat', 'fish', 'tea', 'water', 'water', 'water'}
for i in basket:
    print(i)