'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь
d и два числа: key и value.

Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key.
Если и ключа 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне её не должно быть.
Функция не должна вызывать внутри себя функции input и print.

Пример работы функции:

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
---
print(update_dictionary(d, 0, -5))  # None
print(d)                            # {0: [-5]}  (0*0=2)
update_dictionary(d, 1, -1)
print(d)                            # {0: [-5], 2: [-1]} (тк индекса 1 нет создаем key*2=2)
update_dictionary(d, 2, -2)
print(d)                            # {0: [-5], 2: [-1, -2]} (тк индекс 2 есть добавляем -2 в него)
update_dictionary(d, 3, -3)
print(d)                            # 0: [-5], 2: [-1, -2], 6: [-3]}
'''

def update_dictionary(d, key, value):
    int(key)
    if key in d:
        d[key] += [value]
    elif (key*2) in d:
        d[key*2] += [value]
    else:
        d[key*2] = [value]

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)

'''
Еще примеры решения:

def update_dictionary(d, key, value):
    if key not in d:
        key = 2 * key
    if key not in d:
        d[key] = list()
    d[key].append(value)

---
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d.setdefault(2 * key, []).append(value)

---
def update_dictionary(d, k, v):
    if k in d:
        d.setdefault(k, []).append(v)
    else:
        d.setdefault(k*2, []).append(v)

'''