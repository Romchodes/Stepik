'''
Вывести сумму всех нечетных чисел от a до b (включая обе границы)
'''

a, b = (int(i) for i in input().split())
# a, b = input().split()
# a = int(a)
# b = int(b)
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print(s)

'''
Можно еще так решить:
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)

Для ввода чисел можно использовать List comprehension (редко переводится на русский,
но можно определить как генератор списков).
a, b = (int(i) for i in input().split())
'''